#!/usr/bin/env python3
""" unittests to test if functions are working as expected """
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json


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


class TestGetJson(unittest.TestCase):
    """ mock HTTP calls """
    @parameterized.expand([
       ("http://example.com", {"payload": True}),
       ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        A method to test that utils.get_json returns the expected result
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)
