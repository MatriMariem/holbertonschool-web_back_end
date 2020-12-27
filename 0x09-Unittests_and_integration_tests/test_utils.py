#!/usr/bin/env python3
""" unittests to test if functions are working as expected """
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ class of unittests methods """
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, result):
        """ A method to test the utils.access_nested_map method """
        self.assertEqual(access_nested_map(map, path), result)

    @parameterized.expand([
       ({}, ("a",)),
       ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        self.assertRaises(KeyError, access_nested_map, map, path)
