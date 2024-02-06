#!/usr/bin/python3
"""
Module contains a script that takes in a letter
And sends a POST request to a URL with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    args = ""
    data = {}
    if (len(sys.argv) != 1):
        args = sys.argv[1]
        data = {'q': args}
    else:
        data['q'] = args

    try:
        response = requests.post(url, data)
        if not response.json():
            print('No result')
        else:
            r_id = response.json().get('id')
            r_name = response.json().get('name')
            print(f"[{r_id}] [{r_name}]")
    except Exception:
        print('Not a valid JSON')
