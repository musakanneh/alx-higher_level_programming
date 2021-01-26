#!/usr/bin/python3
"""Test cases for Square class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import io
import json
import os
from contextlib import redirect_stdout


class TestBaseClass_to_json(unittest.TestCase):

    """Test Base"""

    def setUp(self):
        """Resets __nb_objects"""
        Base.reset()

    def test_convert(self):
        """Checks from_jon_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_convert_empty(self):
        """Checks from_jon_string"""
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_convert_none(self):
        """Checks from_jon_string"""
        list_input = None
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])

        list_output = Rectangle.from_json_string(23)
        self.assertEqual(list_output, [])

    def test_exceptions(self):
        """Test exceptions"""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

        with self.assertRaises(TypeError):
            Rectangle.from_json_string(32, 443)

        with self.assertRaises(TypeError):
            Square.from_json_string()

        with self.assertRaises(TypeError):
            Square.from_json_string(32, 443)

    def test_convert_empty_string(self):
        """Checks from_jon_string"""
        list_output = Rectangle.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_convert_return_(self):
        """Checks from_jon_string"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))
