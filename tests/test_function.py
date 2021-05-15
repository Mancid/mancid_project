import unittest
from backend.function.dict_url import dict_url


class BasicTest(unittest.TestCase):

    def test_dict_url(self):
        self.assertIsInstance(dict_url(), dict)
