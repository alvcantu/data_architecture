# transform queries and push into permanent queries table
# user_type, user_category, query_type, schemas, tables
# for those queries ran with dbt, check the tags at the beginning of the query to determine if test or not and to which model they belong to.
# for the rest scan the query to find schemas.tables, ingestion ones should be after INSERT INTO
# Classify each query done by explore or external tool by has_filtering (contains where or having)