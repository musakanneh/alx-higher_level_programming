#!/usr/bin/python3
"""Test cases for Rectangle class, task 7"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
import io
from contextlib import redirect_stdout
from models.base import Base


class TestRectangleClassDisplay(unittest.TestCase):

    """Test cases for rectangle, task 7"""

    def tearDown(self):
        """Teardown"""
        Base.reset()

    def test_display(self):
        """Test display with valid arguments"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 3
        r1 = Rectangle(4, 3)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 2) + (" " * 2 + '#' * 2 + '\n') * 3
        r1 = Rectangle(2, 3, 2, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 0) + (" " * 2 + '#' * 2 + '\n') * 3
        r1 = Rectangle(2, 3, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_draw(self):
        """Test square with the size of 1"""
        f = io.StringIO()
        s = ('#' * 1 + '\n') * 1
        r1 = Rectangle(1, 1)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

    def test_square(self):
        """Test if square is inheriting display method"""
        f = io.StringIO()
        s = ('#' * 4 + '\n') * 4
        r1 = Square(4)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)

        f = io.StringIO()
        s = ('\n' * 2) + (" " * 2 + '#' * 2 + '\n') * 2
        r1 = Square(2, 2, 2)
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), s)
