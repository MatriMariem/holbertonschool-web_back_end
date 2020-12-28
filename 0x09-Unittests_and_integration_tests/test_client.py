#!/usr/bin/env python3
""" unittests to test if functions are working as expected """
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ class of unittests methods """
    @parameterized.expand([
       ("google"),
       ("abc")
    ])
    # @patch('utils.requests.get')
    def test_org(self, org):
        """ test_org method to test """
        g = GithubOrgClient(org)
        self.assertEqual(g.org(), "https://api.github.com/orgs/{}".format(org))
