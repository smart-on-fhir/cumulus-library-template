# https://docs.smarthealthit.org/cumulus/library/workflows/file_upload.html
# config_type specifies what workflow syntax to use
config_type="file_upload"
# we're declaring a new table, template__encounter_valueset (the prefix is auto applied)
[tables.encounter_valueset]
# we specify which file to upload to create the table against
file = "../data/encounter_class_valueset.tsv"
# if its csv-like and not comma delimited, we can specify the delimiter
delimiter = "\t"