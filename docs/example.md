# Example files

This document aims to run through some of the examples included in this repository,
which show off some of the more common patterns for how you'd include queries in
a study. We'll walk through each type individually

## Study manifest

The manifest defines what will be built when, in what order. Here's 
[the version from the template study](../cumulus-library-template/manifest.toml), 
with the commenting stripped out:

```toml
study_prefix = "template"

[file_config.file_names]
"external data" = [
    "workflows/upload_encounter_class.toml"    
]
"study cohort" = [
  "queries/patients.sql",
]
"other resources for patients" =[
    "builders/conditions.py",
    "queries/encounters.sql",
]
"metadata_tables" = [
    "queries/meta_date.sql",
    "queries/meta_version.sql",
]
counts = [
    "builders/count_conditions.py",
    "builders/count_encounters.py",
]

[export_config]
count_list = [
    "template__count_condition",
]
annotated_count_list = [
    "template__count_encounter_annotated",
]
meta_list = [
  "template__meta_date",
  "template__meta_version",
]
```

This is doing three things:
- specifying the study prefix
- specifying stages to run as groups of independent steps
- providing a list of tables to export. They are organized by type, which we use when
  we ship those files off for aggregation.

If something isn't in your manifest, it won't be run by the library tooling.

## Using raw SQL

You can always just give a study a SQL query to run. You probably have some data in DuckDB
or Athena, so you can iterate on queries there until you find something, and then drop it
into a study.

There are no restrictions on this, but be aware that differences between DBs/datasources
can cause queries to be brittle, so try to use this method for simple queries only. We
have some 
(guidelines for writing SQL)[https://docs.smarthealthit.org/cumulus/library/writing-sql.html]
that may help with some common pitfalls.

## Using python builders

Python builders are more complex than writing SQL, but provide a couple of benefits:
- The library provides a lot of templates, which handle some of the complex cases
  out of the box
- If you need a query to react to the contents of a database, you can run a query,
  and then change the value you pass to a template based on the contents of that query
- Builders can inherit from others, so you can share some common functionality without
  reinventing the wheel.

There are two kinds of example of this in the 
[builders](../cumulus-library-template/builders)
directory:
- [conditions.py](../cumulus-library-template/builders/conditions.py)
  is providing a basic join between two tables
- [count_conditions.py](../cumulus-library-template/builders/count_conditions.py)
  and
  [count_encounters.py](../cumulus-library-template/builders/count_encounters.py)
  both use the
  [CountsBuilder](https://docs.smarthealthit.org/cumulus/library/api.html#countsbuilder)
  class to create powerset count tables. count_encounter.py also shows using an annotation
  to add additional metadata to a table.


## Using workflows

Chances are, you're going to have :something: from a third party source - a list of codes,
some analysis from another system, maybe something an SME manually IDed, that you want to
include in a study.

We provide a
[workflow](https://docs.smarthealthit.org/cumulus/library/workflows.html)
for this. The goal of these generally is to turn something with a bunch of complex
steps into a simple config file. You can read more details about this specific workflow
in the 
[project docs](https://docs.smarthealthit.org/cumulus/library/workflows/file_upload.html), 
but most cases will look like
[our example](../cumulus-library-template/workflows/upload_encounter_class.toml), which
is just uploading a subset of the FHIR encounter class valueset that we're using to select
from all available encounters
```toml
config_type="file_upload"
[tables.encounter_valueset]
file = "../data/encounter_class_valueset.tsv"
delimiter = "\t"
```

Here, we add a table named `encounter_valueset` to the list of file-driven tables, and provide
two arguments - a file path to the raw source, and the delimiter used in the file. 
For local builds you don't need anything else. For remote builds you'll need an active
AWS session key in your profile; they way to do this will value by organization, so talk to
your IT folks about it.

Workflows can do a lot of very different things, so each kind will require different arguments. The docsite is the best place for more details about this.