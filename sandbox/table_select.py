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


# Select with a parameterized WHERE clause and wildcard
sql = "SELECT * FROM customers WHERE email LIKE %s"
adr = ("%example.com", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)     