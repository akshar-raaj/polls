from django.test import Client


def test_polls():
    client = Client()
    response = client.get('/polls/')
    assert response.status_code == 200