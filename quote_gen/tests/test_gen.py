from conftest import client


def test_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200


def test_quote_returned(client):
    response = client.get('/get-quote')
    data = response.json
    results = data['results']
    array = []
    for result in results:
        array.append(result)
    assert array.size                   #assert array is not empty