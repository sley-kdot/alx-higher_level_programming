#!/usr/bin/python3
"""
Module contains a script that takes in a URL, sends a request to the URL
Displays the body of the response
Manages urllib.error.HTTPError exceptions
print: Error code: followed by the HTTP status code
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
