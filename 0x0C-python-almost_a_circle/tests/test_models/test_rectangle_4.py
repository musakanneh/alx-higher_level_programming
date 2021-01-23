#!/usr/bin/python3
"""Test model for the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Testing the area of the rectangle"""

    def test_area(self):
        """Tests the area of the rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(10, 10)
        self.assertEqual(r3.area(), 100)

    def test_multi_area(self):
        """Testing for multiple areas"""
        pass


if __name__ == '__main__':
    unittest.main()
