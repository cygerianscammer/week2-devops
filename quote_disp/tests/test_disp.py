from conftest import app

def test_status_code(app):
    response = app.get('/')
    assert response.status_code == 200


def test_health_endpoint(app):
    response = app.get('/health')
    data = response.data.decode() 
    assert data == "healthy"