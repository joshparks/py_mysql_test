import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin"
)

#print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS py_db_test")

mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)