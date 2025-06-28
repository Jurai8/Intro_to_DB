import mysql.connector

def main():
    # connect first
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root@localhost",
        password="Guiltiasinjurai14@",
        
        )

    except mysql.connector.Error as err:
        print(f"Could not connect to db: {err}")
        
    

    cursor = mydb.cursor()

    # create the db
    try:
        cursor.execute("""
        CREATE DATABASE IF NOT EXISTS alx_book_store
        """
        )

        print("Database 'alx_book_store' created successfully!")
        
    except Exception as err:
        print(f"Could not create db: {err}")


    # connect to the db after creating it
    try:
        cursor.execute("USE alx_book_store")
        print("Switched to database 'alx_book_store'.")
    except mysql.connector.Error as err:
        print(f"Could not switch to database 'alx_book_store': {err}")


    cursor.execute("""
    CREATE TABLE Books (
        book_id INT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT, 
        price DOUBLE,
        publication_date DATE, 

        FOREIGN KEY (author_id) REFERENCES Authors (author_id) /* This tells sql that we're referencing the primary key in a different table */
    )
    """
    )

    cursor.execute("""
    CREATE TABLE Authors (
        author_id INT PRIMARY KEY,
        author_name VARCHAR(215)
    )
    """
    )

    cursor.execute("""
    CREATE TABLE Customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(215),
        email VARCHAR(215),
        address TEXT
    )
    """
   )
    
    cursor.execute("""
    CREATE TABLE Orders (
        order_id INT PRIMARY KEY,
        customer_id INT, 
        order_date DATE,

        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    ) 
    """
    )

    cursor.execute("""
    CREATE TABLE Order_Details (
        orderdetailid INT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity DOUBLE,

        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
    """
    )


    cursor.close()
    mydb.close()
    


if __name__ == '__main__':
    main()