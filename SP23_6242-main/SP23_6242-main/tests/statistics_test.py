def test_statistics(app, client):
    res = client.get('/statistics/')
    assert res.status_code == 200
