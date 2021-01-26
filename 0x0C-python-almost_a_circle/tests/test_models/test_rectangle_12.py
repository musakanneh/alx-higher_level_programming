#!/usr/bin/python3
"""Test cases for Square class"""
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

    def test_args_order(self):
        """Checks correct order of arguments"""
        f = io.StringIO()
        s = "[Square] (10) 10/10 - 89"
        r1 = Square(10, 10, 10, 10)
        r1.update(size=89)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(size=1, x=2)
        f = io.StringIO()
        s = "[Square] (10) 2/10 - 1"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(y=1, size=2, x=3, id=89)
        f = io.StringIO()
        s = "[Square] (89) 3/1 - 2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(x=1, size=2, y=3)
        f = io.StringIO()
        s = "[Square] (89) 1/3 - 2"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, str"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = [32, 32]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = (2, 3)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = "string"
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, dict"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = 3.14
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(43, 43, 32, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset()
        r1 = Square(10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_area(self):
        """Test for area"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s1.update(2, 4)
        self.assertEqual(s1.area(), 16)

    def test_wrong_keywords(self):
        """Test keywords"""
        s1 = Square(10, 2, 1)
        s1.update(key=23, school=32)
        self.assertEqual(getattr(s1, "key", 0), 0)
        self.assertEqual(getattr(s1, "school", 0), 0)

    def test_many_args(self):
        """Test with too many arguments"""
        r1 = Square(10, 10)
        r1.update(10, 10, 10, 10, 10, 10, 10, 10)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 10")

    def test_args_value_zero_1(self):
        """Check valid value"""
        msg = " must be > 0"
        err = ValueError
        try:
            Square(-10)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)

        try:
            Square(0)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)

        msg = " must be >= 0"
        try:
            Square(10, -2)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            Square(10, 2, -3)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)
