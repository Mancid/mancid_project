import unittest
import pymongo
from mock import patch


class MyMongo(object):
    def initialize(self):
        try :
            self.client = pymongo.MongoClient("127.0.0.1", 27017)
            self.conn = self.client["DB_TEST"]
        except Exception:
            print("Except in initialize !")
            return False
        return True

class TestMymongo(unittest.TestCase):
    def test_mongodb_initialize(self):
        with patch("pymongo.MongoClient") as mock_mongo:
            self.mymongo = MyMongo()
            self.assertEqual(self.mymongo.initialize(), True)

