from getpass import getpass
from mysql.connector import connect, Error

def get_connection(db_name="py_db_test"):
    try:
        connection = connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database=db_name
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
