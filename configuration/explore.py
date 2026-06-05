# if file ran with no generated token run bash connetcing to postgress with development_{developer_name}
# else read table with data_access_users to see if token eists and is still valid
    # if so output all schemas that contain the email_address inside data_access_users inside products.yml
    # ask user for schema, then output all data products available and ask for which one to explore