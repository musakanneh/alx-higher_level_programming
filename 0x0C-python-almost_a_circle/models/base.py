#!/usr/bin/python3
"""Base class"""

import json
import os
import csv
import turtle


class Base:
    """Represents the base class

    Observation:
        The class is used to manage id attribute
        in all your future classes and to avoid duplicating
        the same code (by extension, same bugs)

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates the id class with

        Args:
            id(int): the class id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries(list): list of dictionary

        """
        if list_dictionaries is None or list_dictionaries is " ":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of
        list_objs to a file

        Args:
            list_objs(): a list of instances who inherits ofBase -
            example: list of Rectangle or list of Square instances

        """
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string

        Args:
            json_string(str): a string representing a list
            of dictionaries

        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary(pointer): can be thought of as a
            double pointer to a dictionary

        """
        if cls.__name__ == "Rectangle":
            result = cls(32, 3)
            result.update(**dictionary)
            return result
        if cls.__name__ == "Square":
            result = cls(32)
            result.update(**dictionary)
            return result

    @classmethod
    def load_from_file(cls):
        """A class method that returns a
        list instance

        """
        list_instance = []
        file_name = cls.__name__ + ".json"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                s = cls.from_json_string(file.read())
            for i in s:
                list_instance.append(cls.create(**i))
            return list_instance
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A  class method that serializes and
        deserializes in CSV

        """
        if (list_objs is None or not isinstance(list_objs, list)
                or not all(isinstance(j, Base) for j in list_objs)):
            with open(cls.__name__ + ".csv", "w") as file:
                file.write("[]")
        if list_objs and any(isinstance(j, Base) for j in list_objs):
            dict_data = [i.to_dictionary() for i in list_objs]
            if cls.__name__ == "Rectangle":
                csv_columns = ["id", "width", "height", "x", "y"]
            else:
                csv_columns = ["id", "size", "x", "y"]
            with open(cls.__name__ + ".csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        list_instance = []
        name = cls.__name__ + ".csv"
        if os.path.isfile(name):
            with open(name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws sqaures and rectangles"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()
