import pytest
from app import app
import requests

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
    url = 'http://localhost:5001/toxicity/result?sentence=TEST'
    resp = requests.get(url)
    assert resp.url == 'http://localhost:5001/toxicity/result?sentence=TEST'
    assert resp.status_code == 200