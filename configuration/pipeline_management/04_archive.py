# Extract latest archive date for each schema in the database
# if none or today> (latest archive date + 45 days) then proceed to analyize that schema
# Scan schema.yml to categorize tables between those with generated_at and those without + extract all relationships
# Scan all queries that contain table with generated at, if none have has_filtering=1 then skip, else extract earliest date of generated at being filtered
# From the tables with earliest date of genarated_at above, extract all primary keys of those values to be filtered out
# archive those primary keys with their connnected tables (using relationships) that do not contain a genarated_at

