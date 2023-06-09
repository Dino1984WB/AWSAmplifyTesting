#main backend file for the website

import requests
import mysql.connector

#print http request contents to console (debugging)
def print_http_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-successful status codes

        print("HTTP Response:")
        print(response.text)  # Print the response content

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

#target website URL         
url = "https://main.doz45kizuqzer.amplifyapp.com/"
print_http_response(url) #print http contents to console


#mysql | write 'item' to db from string converted from json found in http req

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

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

#add call for write_string _to_database() here