from flask_login import current_user
from tests.base import BaseTest

class MyTests(BaseTest):
  def test_a(self):
    with self.app:
      return current_user
