#!/usr/bin/python3
"""
Python script that takes in a string and sends
a search request to the Star Wars API, with pagination
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    j = r.json()
    l = j.get('results')
    print('Number of results:', j.get('count'))
    while j.get('next') is not None:
        r = requests.get(j.get('next'))
        j = r.json()
        l += j.get('results')
    for i in l:
        print(i.get('name'))
