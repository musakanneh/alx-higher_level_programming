#!/usr/bin/python3
"""Test cases for Square class"""


import unittest
import inspect
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
import json
import os
from contextlib import redirect_stdout


class TestBaseClass_to_json(unittest.TestCase):
    """Test Base"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_exceptions(self):
        """Test exceptions"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        with self.assertRaises(TypeError):
            Rectangle.load_from_file(list_rectangles_input, 32, 3212)

        r1 = Square(10, 7, 2)
        r2 = Square(2)
        list_rectangles_input = [r1, r2]

        with self.assertRaises(TypeError):
            Square.load_from_file(list_rectangles_input, 32, 3212)

    def test_aaaaaa_no_file(self):
        """Test if there is no file"""
        file = "Rectangle.json"
        if os.path.isfile(file):
            os.remove(file)
        out = Rectangle.load_from_file()
        self.assertEqual(out, [])

        file = "Square.json"
        if os.path.isfile(file):
            os.remove(file)
        out = Square.load_from_file()
        self.assertEqual(out, [])

    def test_types(self):
        """"Test types"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_output = Rectangle.load_from_file()
        self.assertTrue(type(list_output))
        self.assertTrue(all(isinstance(i, Base) for i in list_output))

        r1 = Square(10, 7, 2)
        r2 = Square(2)
        list_rectangles_input = [r1, r2]
        Square.save_to_file(list_rectangles_input)
        list_output = Square.load_from_file()
        self.assertTrue(type(list_output))
        self.assertTrue(all(isinstance(i, Base) for i in list_output))

    def test_valid_data(self):
        """Simple test"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.load_from_file))
