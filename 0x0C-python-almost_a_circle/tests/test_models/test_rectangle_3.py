#!/usr/bin/python3
"""Validate attributes"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the rectangle model"""

    def test_rectangle_value(self):
        """Tests the rectangle value"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)


if __name__ == '__main__':
    unittest.main()
