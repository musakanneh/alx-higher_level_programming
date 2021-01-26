#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquareClass_dict(unittest.TestCase):
    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_dict(self):
        """Test dictionary"""
        d = {'id': 1, 'x': 1, 'size': 10, 'y': 9}
        r1 = Square(10, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(isinstance(r1_dictionary, dict))
        self.assertEqual(d, r1_dictionary)

    def test_exceptions(self):
        """Test exceptions"""
        s1 = Square(10, 2, 1)
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(323232)
