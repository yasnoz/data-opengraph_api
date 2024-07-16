# pylint: disable-all

import unittest
from opengraph import fetch_metadata

class TestOpenGraph(unittest.TestCase):
    def test_github_com(self):
        data = fetch_metadata("https://www.github.com")
        self.assertRegex(data["title"], r'(?i)github')

    def test_wrong_url_returns_dict(self):
        data = fetch_metadata("https://www.a.com") # Does not exist
        self.assertIsInstance(data, dict)

    def test_wrong_url_returns_empty_dict(self):
        data = fetch_metadata("https://www.a.com")  # Does not exist
        self.assertEqual(data, {})

    def test_empty_url_returns_dict(self):
        data = fetch_metadata("")
        self.assertIsInstance(data, dict)

    def test_empty_url_returns_empty_dict(self):
        data = fetch_metadata("")
        self.assertEqual(data, {})
