#!/usr/bin/python3
"""
Python script that takes in a letter
and sends a POST request
"""
from sys import argv
import requests


if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
        j = r.json()
        if j:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
