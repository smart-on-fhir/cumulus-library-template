# https://docs.smarthealthit.org/cumulus/library/workflows/counts.html
# config_type specifies what workflow syntax to use
config_type = "counts"
## we're declaring a new table, `count_condition` (the prefix is automatically added)
[tables.count_condition]
# source_table is the table we're selecting from
source_table = "template__condition"
# "description" is optional text describing what the count is attempting to do.
# It will be used as descriptive text by the Cumulus dashboard
description = """An example count table, summarizing the template__condition table."""
# "table_cols" is a list of the columns to select from source_table
table_cols = [
    "code",
    "clinicalstatus_code"
]
# secondary_id allows us to count an additional ID field from the source table
secondary_id = "encounter_ref"
# since the reference test data is small, we'll turn down the bin
# size - but don't do this in a real study, or you'll potentially
# have identifiable data sets
min_subject = 1


[tables.count_encounter]
source_table = "template__encounter"
table_cols = ["class_code", "period_start_year"]
# here, we're adding a code display string to a cube using an annotation
[tables.count_encounter.annotation]
# field is the column from the source table we want to join with
field = "class_code"
# join_table is the table to use for annotation
join_table = 'template__encounter_valueset'
# join_field is the column from the join table to use as the other half of the join
join_field = "code"
# columns is a list of columns to add from the annotating table.
# each column is a list that is either ['name', 'type'] or ['name','type','alias']
columns = [
    ["display","varchar","code_display"]
]