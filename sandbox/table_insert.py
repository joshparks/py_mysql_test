import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin",
    database="py_db_test"
)   

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = [
  ('John Doe', 'john@example.com'), 
  ('Jane Smith', 'jane@example.com'),
  ('Bob Johnson', 'bob@example.com')
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "records inserted.")