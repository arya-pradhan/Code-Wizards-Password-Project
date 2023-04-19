def test_about(app, client):
    res = client.get('/about')
    assert res.status_code == 200
