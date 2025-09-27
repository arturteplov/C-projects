# (STEP 7 • Polish) Basic backend tests
from backend.app import app

def test_ping():
    client = app.test_client()
    r = client.get('/api/ping')
    assert r.status_code == 200
    assert r.get_json()['ok'] is True

def test_submit_missing_fields():
    client = app.test_client()
    r = client.post('/api/submit', json={})
    assert r.status_code == 400
    body = r.get_json()
    assert body['ok'] is False
    assert 'Missing' in body['error']
