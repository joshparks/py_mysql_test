import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="py_db_test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

results = mycursor.fetchall()

for x in results:
    print(x)    