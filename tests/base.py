import unittest
from tests import app, db


class BaseTest(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['LOGIN_DISABLED'] = False
    self.app = app.test_client()
    db.create_all()
