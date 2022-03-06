import pytest
from app import app

client = app.test_client()


def test_toxicity_request_return_form_template():
    rv = client.get('/toxicity/form')
    assert rv.status == '200 OK'
    assert '<title>Toxicity Form</title>' in rv.data.decode('utf-8')


def test_toxicity_form_request_return_form_template():
    rv = client.get('/toxicity/form')
    assert rv.status == '200 OK'
    assert '<title>Toxicity Form</title>' in rv.data.decode('utf-8')

# Would need a separate testing environment to run properly (ip resolution error when calling backend)

# def test_toxicity_result_request_return_result_template_2():
#     rv = client.get('/toxicity/result')
#     assert rv.status == '200 OK'
#     assert '<title>Toxicity Result</title>' in rv.data.decode('utf-8')