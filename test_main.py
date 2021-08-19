
from urlshort import create_app

def test_shorten(client):
    response = client.get('/about')
    assert b'Shorten' in response.data