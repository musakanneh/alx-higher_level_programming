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

    def test_create(self):
        """Test create"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        r1 = Square(3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (3) 1/0 - 3")
        self.assertEqual(str(r2), "[Square] (3) 1/0 - 3")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_wrong(self):
        """Wrong number of args"""
        with self.assertRaises(TypeError):
            Rectangle.create("Hi")

        with self.assertRaises(TypeError):
            Square.create("Go")
        self.assertEqual(Base.create(), None)

    def test_classmethod(self):
        """Checks class method"""
        self.assertTrue(inspect.ismethod(Base.create))

    def test_create_rectangle(self):
        """Test create"""
        d = {'id': 89}
        st = "[Rectangle] (89) 0/0 - 32/3"
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'width': 1}
        st = "[Rectangle] (89) 0/0 - 1/3"
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'width': 1, 'height': 2}
        st = "[Rectangle] (89) 0/0 - 1/2"
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'width': 1, 'x': 3}
        st = "[Rectangle] (89) 3/0 - 1/3"
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        st = "[Rectangle] (89) 3/4 - 1/2"
        r1 = Rectangle.create(**d)
        self.assertEqual(str(r1), st)

    def test_create_square(self):
        """Test create"""
        d = {'id': 89}
        st = "[Square] (89) 0/0 - 32"
        r1 = Square.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'size': 1}
        st = "[Square] (89) 0/0 - 1"
        r1 = Square.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'size': 1}
        st = "[Square] (89) 0/0 - 1"
        r1 = Square.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'size': 1, 'x': 3}
        st = "[Square] (89) 3/0 - 1"
        r1 = Square.create(**d)
        self.assertEqual(str(r1), st)

        d = {'id': 89, 'size': 1, 'x': 3, 'y': 4}
        st = "[Square] (89) 3/4 - 1"
        r1 = Square.create(**d)
        self.assertEqual(str(r1), st)
