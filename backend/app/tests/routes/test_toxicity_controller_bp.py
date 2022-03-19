import pytest
from flask import url_for
from app import app
from controller.toxicityController import undefined_string

client = app.test_client()

toxicity_string = "toxicity"
severe_toxicity_string = "severe_toxicity"
obscene_string = "obscene"
threat_string = "threat"
insult_string = "insult"
identity_attack_string = "identity_attack"

def test_sentiment_form_bp_return_form_template():
    # Simulate a request context to use blueprint
    with app.test_request_context():
        url = url_for('toxicity_bp.default')
    
    rv = client.get(url)
    assert rv.status == '200 OK'
    
def test_sentiment_sentence_check_bp_return_result_template():
    # Simulate a request context to use blueprint
    with app.test_request_context():
        url = url_for('toxicity_bp.toxicity_sentence_check')
    
    rv = client.get(url)
    assert rv.status == '200 OK'
    
    assert toxicity_string in rv.data.decode('utf-8')
    assert severe_toxicity_string in rv.data.decode('utf-8')
    assert obscene_string in rv.data.decode('utf-8')
    assert threat_string in rv.data.decode('utf-8')
    assert insult_string in rv.data.decode('utf-8')
    assert identity_attack_string in rv.data.decode('utf-8')