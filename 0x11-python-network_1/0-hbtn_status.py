#!/usr/bin/python3
"""
a python script that fetches a URL
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as reponse:
        status = reponse.read()
        print("Body response:")
        print(" " * 1, f"- type: {type(status)}")
        print(" " * 1, f"- content: {status}")
        print(" " * 1, f"- utf8 content: {status.decode('utf-8')}")
