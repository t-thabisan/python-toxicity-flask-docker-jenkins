import pytest
from flask import url_for
from app import app
#from controller.sentimentController import form_template, result_template, undefined_string

client = app.test_client()


def test_toxicity_form_bp_return_form_template():
    # Simulate a request context to use blueprint
    with app.test_request_context():
        url = url_for('toxicity_bp.toxicity_form')

    rv = client.get(url)
    assert rv.status == '200 OK'
    assert '<title>Toxicity Form</title>' in rv.data.decode('utf-8')

# Would need a separate testing environment to run properly (ip resolution error when calling backend)

# def test_toxicity_sentence_check_bp_return_result_template():
#     # Simulate a request context to use blueprint
#     with app.test_request_context():
#         url = url_for('toxicity_bp.toxicity_sentence_check')
#
#     rv = client.get(url)
#     assert rv.status == '200 OK'
#     assert '<title>Toxicity Result</title>' in rv.data.decode('utf-8')

