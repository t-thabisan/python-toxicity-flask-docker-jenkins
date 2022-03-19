import pytest
from flask import url_for
from app import app
from controller.toxicityController import default_string

client = app.test_client()

toxicity_string = "toxicity"
severe_toxicity_string = "severe_toxicity"
obscene_string = "obscene"
threat_string = "threat"
insult_string = "insult"
identity_attack_string = "identity_attack"

def test_default_return_default_string():
    rv = client.get('/api/default')
    assert rv.status == '200 OK'
    assert default_string == rv.data.decode('utf-8')

def test_toxicity_sentence_check_return_default_string():
    rv = client.get('/api/toxicity')
    
    assert rv.status == '200 OK'
    
    assert toxicity_string in rv.data.decode('utf-8')
    assert severe_toxicity_string in rv.data.decode('utf-8')
    assert obscene_string in rv.data.decode('utf-8')
    assert threat_string in rv.data.decode('utf-8')
    assert insult_string in rv.data.decode('utf-8')
    assert identity_attack_string in rv.data.decode('utf-8')