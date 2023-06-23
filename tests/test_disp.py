from conftest import client

def test_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get('/health')
    data = response.data.decode() 
    assert data == "healthy"