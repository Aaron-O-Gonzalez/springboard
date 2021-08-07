import mysql.connector
import csv

def get_db_connection():
#Establish connection with MySQL server
#Ensure schema exists prior to connection
    connection = None
    try:
        connection = mysql.connector.connect(user = '<userName>',
                                             password = '<password>',
                                             host ='localhost',
                                             port = '3306',
                                             database = '<db_name>')
        print("Connection successful")
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection

def create_table(connection):
#Creates the table given the defined schema
    sql_statement = """CREATE TABLE IF NOT EXISTS third_party_sales(
                                    ticket_id INT NOT NULL PRIMARY KEY,
                                    trans_date DATE,
                                    event_id INT,
                                    event_name VARCHAR(50),
                                    event_date DATE,
                                    event_type VARCHAR(10),
                                    event_city VARCHAR(20),
                                    customer_id INT,
                                    price DECIMAL,
                                    num_tickets INT)
                     """
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    cursor.close()
    return

def load_third_party(connection, csv_path):
#Insert values into table created from the create_table function
    cursor = connection.cursor()
    with open(csv_path) as csv_file:
        fileReader = csv.reader(csv_file)
        for line in fileReader:
            ticket_id = line[0]
            trans_date = line[1]
            event_id = line[2]
            event_name = line[3]
            event_date = line[4]
            event_type = line[5]
            event_city = line[6]
            customer_id = line[7]
            price = line[8]
            num_tickets = line[9]
            
            sql_statement = """INSERT INTO third_party_sales(ticket_id, trans_date, event_id, 
                                                         event_name, event_date, event_type,
                                                         event_city,customer_id, price, num_tickets)
                                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            values = (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets)
            cursor.execute(sql_statement, values)
        connection.commit()
    cursor.close()

def query_popular_tickets(connection):
#Get the three most popular tickets in the past month
    sql_statement = """SELECT event_name FROM third_party_sales
                        GROUP BY event_name
                        ORDER BY COUNT(event_name) DESC
                        LIMIT 3"""

    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

connection = get_db_connection()
create_table(connection)
load_third_party(connection, 'third_party_sales_1.csv')
popular_tickets = query_popular_tickets(connection)

print("Here are the most popular tickets in the past month:\n- {}\n- {}\n- {}".format(popular_tickets[0][0], popular_tickets[1][0], popular_tickets[2][0]))