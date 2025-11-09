from db.connection import get_connection, close_connection

# Create a new customer
def create_customer(name, email, age):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO customers (name, email, age) VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, email, age))
    connection.commit()
    print(f"Customer {name} added successfully.")   
    close_connection(connection)

# Retrieve a customer by ID
def get_customer_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT id, name, email, age FROM customers WHERE id = %s"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    if result:
        print(f"Found Customer - ID: {result[0]}, Name: {result[1]}, Email: {result[2]}, Age: {result[3]}")
        customer = {
            "id": result[0],
            "name": result[1],
            "email": result[2],
            "age": result[3]
        }
        close_connection(connection)
        return customer
    else:
        close_connection(connection)
        return None

# Retrieve all customers    
def get_customers():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM customers"
    cursor.execute(query)
    results = cursor.fetchall()
    #for row in results:
        #print(row)
    close_connection(connection)
    return results

# Update customer details
def update_customer(user_id, name=None, email=None, age=None):
    connection = get_connection()
    cursor = connection.cursor()
    updates = []
    if name:
        updates.append(f"name = '{name}'")
    if email:
        updates.append(f"email = '{email}'")
    if age:
        updates.append(f"age = {age}")
    
    if updates:
        query = f"UPDATE customers SET {', '.join(updates)} WHERE id = {user_id}"
        cursor.execute(query)
        connection.commit()
        print(f"Customer with ID {user_id} updated successfully.")
    close_connection(connection)

# Delete a customer by ID
def delete_customer(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM customers WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print(f"Customer with ID {user_id} deleted successfully.")
    close_connection(connection)