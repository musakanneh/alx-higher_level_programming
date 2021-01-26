#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout


class TestRectangleClass_dict(unittest.TestCase):

    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_dict(self):
        """Test dictionary"""
        d = {'y': 9, 'id': 1, 'height': 2, 'width': 10, 'x': 1}
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(isinstance(r1_dictionary, dict))
        self.assertEqual(d, r1_dictionary)

    def test_exceptions(self):
        """Test exceptions"""
        s1 = Rectangle(10, 2, 1)
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(323232)
