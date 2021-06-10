import unittest
import requests
from mock import patch
from tests import url_exists
from backend.function.dict_url import dict_url
from backend.function.parse_xml import xml_parse_url, create_dict


class BasicTest(unittest.TestCase):

    def test_dict_url(self):
        res = {'Antigone': 'https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_ANTI.xml',
               'Pitot': 'https://data.montpellier3m.fr/sites/default/files/ressources/FR_MTP_PITO.xml',
               'Vicarello': 'https://data.montpellier3m.fr/sites/default/files/ressources/FR_CAS_VICA.xml'}
        self.assertIsInstance(dict_url("tests/url_test.ini"), dict)
        self.assertEqual(dict_url("tests/url_test.ini"), res)

    def test_xml_parse_url(self):
        url1 = "https://data.montpellier3m.fr/sites/default"\
               "/files/ressources/FR_MTP_ANTI.xml"
        res1 = "Open"
        url2 = "https://data.montpellier3m.fr/sites/default"\
               "/files/ressources/FR_MTP_CIRCE.xml"
        res2 = "Open"
        url3 = "https://data.montpellier3m.fr/sites/default"\
               "/files/ressources/FR_MTP_OCCI.xml"
        res3 = "Open"
        self.assertIsInstance(xml_parse_url(url1), dict)
        self.assertEqual(xml_parse_url(url1)['Status'], res1)
        self.assertEqual(xml_parse_url(url2)['Status'], res2)
        self.assertEqual(xml_parse_url(url3)['Status'], res3)

    def test_response_url(self):
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            url1 = "https://data.montpellier3m.fr/sites/default"\
                   "/files/ressources/FR_MTP_ANTI.xml"
            url2 = "https://data.montpellier3m.fr/sites/default"\
                   "/files/ressources/FR_MTP_CIRCE.xml"
            url3 = "https://data.montpellier3m.fr/sites/default"\
                   "/files/ressources/FR_MTP_OCCI.xml"
        self.assertTrue(url_exists(url1))
        self.assertTrue(url_exists(url2))
        self.assertTrue(url_exists(url3))

    def test_create_dict(self):
        self.assertIsInstance(create_dict(dict_url("tests/url_test.ini")), dict)
