from app import app

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Ol\xc3\xa1, Mundo!'

def healthcheck():
    response = app.test_client().get('/healthcheck')
    assert response.status_code == 200
    assert response.data == b'{"status": "ok"}'