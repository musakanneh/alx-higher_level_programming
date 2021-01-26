#!/usr/bin/python3
"""Test cases for Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquareClass_size(unittest.TestCase):
    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_setter(self):
        """Checks setter"""
        s1 = Square(5)
        self.assertEqual(s1._Rectangle__width, 5)

    def test_getter(self):
        """Checks getter"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_exceptions_0(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be an integer"
        err = TypeError
        try:
            s1.size = "32322"
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))

    def test_exceptions_1(self):
        """Test exceptions"""
        s1 = Square(5)
        msg = "width must be > 0"
        err = ValueError
        try:
            s1.size = -32
        except Exception as e:
            self.assertEqual(str(e), msg)
            self.assertTrue(isinstance(e, err))
