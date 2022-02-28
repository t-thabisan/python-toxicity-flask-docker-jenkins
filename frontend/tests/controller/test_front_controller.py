import pytest
from app import app

client = app.test_client()


def test_sentiment_request_return_form_template():
    rv = client.get('/toxicity/form')
    assert rv.status == '200 OK'
    assert '<title>Toxicity Form</title>' in rv.data.decode('utf-8')


def test_sentiment_form_request_return_form_template():
    rv = client.get('/toxicity/form')
    assert rv.status == '200 OK'
    assert '<title>Toxicity Form</title>' in rv.data.decode('utf-8')


def test_sentiment_result_request_return_result_template_2():
    rv = client.get('/toxicity/result?sentence=TEST')
    assert rv.status == '200 OK'
    assert '<title>Toxicity Result</title>' in rv.data.decode('utf-8')