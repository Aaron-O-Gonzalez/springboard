#Data Pipeline Mini Project

##Purpose
The Python code file **mini_pipeline.py** is a small data pipeline which assumes the presence of a MySQL database and (1) creates a table with schema for **third_pary_sales_1.csv**, 
(2) inserts the contents of the CSV file into the table, and (3) runs a basic query on the updated table.

##User Requirements
The _get_db_connection()_ function requires three user inputs: userName, password, and db_name. These three inputs vary from each user depending on his/her MySQL settings.

##Dependencies
-Python3.7+
Modules: 
  -csv
  -mysql.connector
  
