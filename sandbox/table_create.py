import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="py_db_test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)