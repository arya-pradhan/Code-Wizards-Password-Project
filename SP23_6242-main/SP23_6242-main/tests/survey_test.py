def test_survey_page(app, client):
    res = client.get('/survey/')
    assert res.status_code == 200


def test_survey_form_page(app, client):
    res = client.get('/survey/form')
    assert res.status_code == 200
