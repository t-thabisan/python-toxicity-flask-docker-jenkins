from flask import render_template, redirect, url_for, request, abort

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

    # Call toxicity back-end
    # multiply values by 100
    scores = {"toxic": 20, "severe_toxic": 11, "obscene": 0, "threat": 1, "insult": 50.0, "identity_hate": 0.0}

    return render_template(result_template,
                           toxic=scores["toxic"],
                           severe_toxic=scores["severe_toxic"],
                           obscene=scores["obscene"],
                           threat=scores["threat"],
                           insult=scores["insult"],
                           identity_hate=scores["identity_hate"],
                           sentence=sentence)
