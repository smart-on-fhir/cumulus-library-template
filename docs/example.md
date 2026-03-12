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

[[stages.default]]
type = "build:parallel"
description = "external data"
files = [
    "workflows/upload_encounter_class.workflow"    
]

[[stages.default]]
type = "build:parallel"
description = "study cohort"
files = [
  "queries/patients.sql",
]

[[stages.default]]
type = "build:serial"
description = "other resources for patients"
files=[
    "builders/conditions.py",
    "queries/encounters.sql",
]

[[stages.default]]
type = "build:parallel"
description = "metadata_tables"
files= [
    "queries/meta_date.sql",
    "queries/meta_version.sql",
]

[[stages.default]]
type = "build:parallel"
description = "metadata_tables"
files = ["workflows/counts.workflow"]

[[stages.default]]
type = "export:counts"
description = "condition count tables"
tables = [
    "template__count_condition",
]

[[stages.default]]
type = "export:annotated_counts"
description = "annotated encounter count tables"
tables = [
    "template__count_encounter_annotated",
]

[[stages.default]]
type = "export:meta"
description = "metadata tables"
tables = [
  "template__meta_date",
  "template__meta_version",
]
```

This is doing two things:
- specifying the study prefix
- specifying a stage, containing a list of actions, which are used in building/exporting tables

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

There is an example of this in the 
[builders](../cumulus-library-template/builders)
directory:
- [conditions.py](../cumulus-library-template/builders/conditions.py)
  is providing a basic join between two tables

## Using workflows

Chances are, you're going to have :something: from a third party source - a list of codes,
some analysis from another system, maybe something an SME manually IDed, that you want to
include in a study. You probably also want to generate some count outputs

We provide
[workflows](https://docs.smarthealthit.org/cumulus/library/workflows.html)
for this. The goal of these generally is to turn something with a bunch of complex
steps into a simple config file.

Each workflow contains a link to the workflow documentation and comments describing general usage.
Workflows can do a lot of very different things, so each kind will require different arguments. The docsite is the best place for more details about this.