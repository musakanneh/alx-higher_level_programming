#!/usr/bin/python3
"""Test cases for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
from contextlib import redirect_stdout


class TestSquareClass_init(unittest.TestCase):

    """Test Square"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_init_0(self):
        """Test init of Rectangle"""
        s1 = Square(5)
        st = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(s1), st)

    def test_init_1(self):
        """Test init of Rectangle"""
        s1 = Square(5, 5)
        st = "[Square] (1) 5/0 - 5"
        self.assertEqual(str(s1), st)

    def test_attr_0(self):
        """Test attr of Rectangle"""
        s1 = Square(5)
        self.assertEqual([s1.width, s1.height], [5, 5])

    def test_attr_1(self):
        """Test attr of Rectangle, size should not created"""
        s1 = Square(2)
        with self.assertRaises(AttributeError):
            print(s1._Square__size)

    def test_attr_str(self):
        """Test attr of Square, size should not created"""
        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "1")

        with self.assertRaises(TypeError):
            Square(1, 2, "1")

    def test_inheritence(self):
        """Tests if Square is child of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            s1 = Square(10, 2, 1, 32, 233232)

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_attr_value(self):
        """Test attr of Square"""
        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -1)

        with self.assertRaises(ValueError):
            Square(1, 2, -1)

        with self.assertRaises(ValueError):
            Square(0)
