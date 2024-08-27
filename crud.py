import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)

cursor = db_connection.cursor()

create_database_query = "CREATE DATABASE test_db"
cursor.execute(create_database_query)

db_connection.commit()

cursor.close()
db_connection.close()