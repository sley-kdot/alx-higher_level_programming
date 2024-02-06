#!/usr/bin/pyhton3
""""
Module contains a script that takes in a URL and an email address
Sends a POST request to the passed URL with the email as a parameter
And finally displays the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    response = requests.post(url, data)
    print(response.text)
