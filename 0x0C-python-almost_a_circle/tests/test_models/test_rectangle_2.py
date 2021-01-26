#!/usr/bin/python3
"""Test model for the rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Tests the rectangle model"""

    def test_id(self):
        """Tests for Id"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_multi_id(self):
        """Tests for valid input"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_valid_params(self):
        """Test for valid parameters"""
        # r4 = Rectangle(3, 5, 2, 8, 108)
        # self.assertEqual([r4.width, r4.height,
        # r4.x, r4.y, r4.id],
        #                  [3, 5, 2, 8, 108])
        # r6 = Rectangle(43, 23)
        # self.assertEqual([r6.width, r6.height],
        # [43, 23])
        pass

    def test_default_params(self):
        """Tests for default paramsters"""
        pass


if __name__ == '__main__':
    unittest.main()
