#!/usr/bin/python3
"""
module contains a script that takes in a URL, sends a request to the URL
and displays the value
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers["X-Request-Id"])
