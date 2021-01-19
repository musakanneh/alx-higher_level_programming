#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """A JSON to string function

    Return:
        the JSON representation of an object (string):

    """
    return json.dumps(my_obj)
