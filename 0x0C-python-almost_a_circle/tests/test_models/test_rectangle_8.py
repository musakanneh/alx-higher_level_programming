#!/usr/bin/python3
"""Test cases for r1.update class, task 8"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestRectangleClass_Update(unittest.TestCase):

    """Test cases for rectangle, task 8"""

    def tearDown(self):
        """Teardown"""
        Base.reset()

    def test_args_order(self):
        """Checks correct order of arguments"""
        Base.reset()
        f = io.StringIO()
        s = "[Rectangle] (89) 10/10 - 10/10"
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(89, 2)
        f = io.StringIO()
        s = "[Rectangle] (89) 10/10 - 2/10"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(89, 2, 3)
        f = io.StringIO()
        s = "[Rectangle] (89) 10/10 - 2/3"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(89, 2, 3, 4)
        f = io.StringIO()
        s = "[Rectangle] (89) 4/10 - 2/3"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

        r1.update(89, 2, 3, 4, 5)
        f = io.StringIO()
        s = "[Rectangle] (89) 4/5 - 2/3"
        with redirect_stdout(f):
            print(r1, end="")
        self.assertEqual(f.getvalue(), s)

    def test_args_valid_types_str(self):
        """Check valid types, str"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
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
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_list(self):
        """Check valid types, list"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = [32, 43]
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_set(self):
        """Check valid types, set"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = {32, 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_tuple(self):
        """Check valid types, tuple"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = (32, 43)
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_dict(self):
        """Check valid types, dict"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = {"Hi": 43}
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_float(self):
        """Check valid types, float"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
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
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_valid_types_none(self):
        """Check valid types, dict"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = None
        msg = " must be an integer"
        err = TypeError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)

    def test_args_value_zero(self):
        """Check valid value"""
        Base.reset()
        r1 = Rectangle(10, 10, 10, 10)
        s = 0
        msg = " must be > 0"
        err = ValueError
        try:
            r1.update(21, s)
        except err as e:
            self.assertEqual((str(e)), "width" + msg)
        try:
            r1.update(21, 32, s)
        except err as e:
            self.assertEqual((str(e)), "height" + msg)
        s = -1
        msg = " must be >= 0"
        try:
            r1.update(21, 32, 43, s)
        except err as e:
            self.assertEqual((str(e)), "x" + msg)
        try:
            r1.update(21, 32, 43, 43, s)
        except err as e:
            self.assertEqual((str(e)), "y" + msg)
