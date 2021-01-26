#!/usr/bin/python3
"""Test cases for Rectangle class, task 6"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout


class TestRectangleClass_Str(unittest.TestCase):

    """Test cases for ractangle, task 6"""

    def setUp(self):
        """Setup, Teardown"""
        Base.reset()

    def test_str_defaults(self):
        """Tests __str__ method"""
        Base.reset()
        f = io.StringIO()
        s = "[Rectangle] (1) 0/0 - 4/3"
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (2) 32/0 - 4/3"
        r2 = Rectangle(4, 3, 32)
        with redirect_stdout(f):
            print(r2, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (3) 3/5 - 4/3"
        r3 = Rectangle(4, 3, 3, 5)
        with redirect_stdout(f):
            print(r3, end="")
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = "[Rectangle] (77) 3/5 - 4/3"
        r77 = Rectangle(4, 3, 3, 5, 77)
        with redirect_stdout(f):
            print(r77, end="")
        self.assertEqual(f.getvalue(), s)
