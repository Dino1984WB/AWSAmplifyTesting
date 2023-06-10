#python program to test db writing to db 'AWSWeb'

import mysql.connector
def write_string_to_database(string):
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            user='dino',  # Replace with your MySQL username
            password='Bilbuk.1994 ',  # Replace with your MySQL password
            database='AWSWeb'  # Replace with your database name
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Define the SQL query to insert the string into the 'items' table
        query = "INSERT INTO items (column_name) VALUES (%s)"

        # Execute the query
        cursor.execute(query, (string,))

        # Commit the changes to the database
        connection.commit()

        print("String inserted successfully!")
        #Close the cursor and connection
        
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)
    
    
    
write_string_to_database("orange")
