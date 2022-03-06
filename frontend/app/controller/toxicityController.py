from flask import render_template, redirect, url_for, request, abort
import requests

form_template = 'request_form.html'
result_template = 'request_response.html'
undefined_string = 'NO SENTENCE DEFINED'


def toxicity_form():
    return render_template(form_template)


def toxicity_sentence_check():
    sentence = request.args.get('sentence')

    # Empty sentence
    if sentence is None:
        sentence = undefined_string

    payload = {'sentence': sentence}
    resp = requests.get('http://service2:5000/api/toxicity', params=payload)
    scores = resp.json()

    # Call toxicity back-end and return result template
    return render_template(result_template,
                           toxic=format(scores["toxicity"]["value"]),
                           severe_toxic=format(scores["severe_toxicity"]["value"]),
                           obscene=format(scores["obscene"]["value"]),
                           threat=format(scores["threat"]["value"]),
                           insult=format(scores["insult"]["value"]),
                           identity_hate=format(scores["identity_attack"]["value"]),
                           sentence=sentence)


def format(value):
    return round(value, 2) * 100
