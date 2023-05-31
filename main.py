#main backend file for the website

import sqlite3
import requests

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