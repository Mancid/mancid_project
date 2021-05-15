import pytest
from backend.main import create_app


@pytest.fixture
def client():
    # db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app = create_app('TESTING')
    app.config['TESTING'] = True

    with app.test_client() as client:
        # with app.app_context():
        yield client

    # os.close(db_fd)
    # os.unlink(app.config['DATABASE'])
