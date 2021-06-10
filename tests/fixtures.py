import pytest
import backend


@pytest.fixture
def client():
  app = backend.create_app('TESTING')
  app.config['TESTING'] = True

  with app.test_client() as client:
    yield client
