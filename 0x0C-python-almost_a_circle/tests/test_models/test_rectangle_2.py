#!/usr/bin/python3
"""Test model for the rectangle class"""
import unittest
from base.models import Rectangle


class TestRectangle(unittest.TestCase):
    """A class test the rectangle model"""

    def test_width(self):
        """Tests for the rectangle's width"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1, 1)
        if r1:
            print("Success!")

    def test_height(self):
        """Test for the rectangle's height"""
        pass


if __name__ == '__main__':
    unittest.main()
