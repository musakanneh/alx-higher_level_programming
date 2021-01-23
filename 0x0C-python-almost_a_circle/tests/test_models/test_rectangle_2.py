#!/usr/bin/python3
"""Test model for the rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """A class test the rectangle model"""

    def test_id(self):
        """Tests for Id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        print()
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
    
    def test_valid_input(self):
        """Tests for valid input"""
        pass


if __name__ == '__main__':
    unittest.main()
