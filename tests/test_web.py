from tests.fixtures import client


def test_index(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Parking' in rv.data
