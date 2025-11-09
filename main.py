import sys
from getpass import getpass
from mysql.connector import connect, Error

from db.connection import close_connection, get_connection
from db.customers import get_customers

def main():
    print("This is the main function.")
    users = get_customers()
    for user in users:
        print(user)

if __name__ == '__main__':
    main()