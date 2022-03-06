import pytest
import json
from model.detoxifyModel import toxicity_check

# SENTENCES
no_toxicity_sentence = "Hello"
max_toxicity_sentence = "Son of a bitch"
severe_toxicity_sentence = "SON OF A BITCH, I WILL CUT YOUR HEAD OFF! I PROMESS!"
obscene_sentence = "This is some big ass !"
threat_sentence = "I will kill you."
insult_sentence = "aha you guys are a bunch of losers."
identity_attack_sentence = "Yet call out all Muslims for the acts of a few will get you pilloried.   So why is it okay to smear an entire religion over these few idiots?  Or is this because it's okay to bash"

# EXPECTED VALUES
#no_toxicity
no_toxicity_sentence_scores = {"toxicity":{"value":0.0},"severe_toxicity":{"value":0.0},"obscene":{"value":0.0},"threat":{"value":0.0},"insult":{"value":0.0},"identity_attack":{"value":0.0}}
#severe_toxicity
severe_toxicity_sentence_scores = {"toxicity":{"value":1.0},"severe_toxicity":{"value":0.66}}
#obscene
obscene_sentence_scores = {"toxicity":{"value":0.98},"obscene":{"value":0.90}}
#threat
threat_sentence_scores = {"toxicity":{"value":0.87}, "threat":{"value":0.86}}
#insult
insult_sentence_scores = {"toxicity":{"value":0.97}, "insult":{"value":0.85}}
#identity_attack
identity_attack_sentence_scores = {"toxicity":{"value":0.85},"identity_attack":{"value":0.55}}

def test_no_toxicity_sentence():
    scores = json.loads(toxicity_check(no_toxicity_sentence))

    assert scores["toxicity"]["value"] >= no_toxicity_sentence_scores["toxicity"]["value"]
    assert scores["severe_toxicity"]["value"] >= no_toxicity_sentence_scores["severe_toxicity"]["value"]
    assert scores["obscene"]["value"] >= no_toxicity_sentence_scores["obscene"]["value"]
    assert scores["threat"]["value"] >= no_toxicity_sentence_scores["threat"]["value"]
    assert scores["insult"]["value"] >= no_toxicity_sentence_scores["insult"]["value"]
    assert scores["identity_attack"]["value"] >= no_toxicity_sentence_scores["identity_attack"]["value"]

def test_max_toxicity(): 
    scores = json.loads(toxicity_check(max_toxicity_sentence))
    assert scores["toxicity"]["value"] == 1.0

def test_severe_toxicity_sentence():
    scores = json.loads(toxicity_check(severe_toxicity_sentence))
    assert scores["toxicity"]["value"] >= severe_toxicity_sentence_scores["toxicity"]["value"]
    assert scores["severe_toxicity"]["value"] >= severe_toxicity_sentence_scores["severe_toxicity"]["value"]
    assert scores["obscene"]["value"] >= 0.0
    assert scores["threat"]["value"] >= 0.0
    assert scores["insult"]["value"] >= 0.0
    assert scores["identity_attack"]["value"] >= 0.0

def test_obscene_sentence():
    scores = json.loads(toxicity_check(obscene_sentence))
    assert scores["toxicity"]["value"] >= obscene_sentence_scores["toxicity"]["value"]
    assert scores["obscene"]["value"] >= obscene_sentence_scores["obscene"]["value"]
    assert scores["severe_toxicity"]["value"] >= 0.0
    assert scores["threat"]["value"] >= 0.0
    assert scores["insult"]["value"] >= 0.0
    assert scores["identity_attack"]["value"] >= 0.0

def test_threat_sentence():
    scores = json.loads(toxicity_check(threat_sentence))
    assert scores["toxicity"]["value"] >= threat_sentence_scores["toxicity"]["value"]
    assert scores["threat"]["value"] >= threat_sentence_scores["threat"]["value"]
    assert scores["severe_toxicity"]["value"] >= 0.0
    assert scores["obscene"]["value"] >= 0.0
    assert scores["insult"]["value"] >= 0.0
    assert scores["identity_attack"]["value"] >= 0.0

def test_identity_attack_sentence():
    scores = json.loads(toxicity_check(identity_attack_sentence))
    assert scores["toxicity"]["value"] >= identity_attack_sentence_scores["toxicity"]["value"]
    assert scores["identity_attack"]["value"] >= identity_attack_sentence_scores["identity_attack"]["value"]
    assert scores["severe_toxicity"]["value"] >= 0.0
    assert scores["obscene"]["value"] >= 0.0
    assert scores["threat"]["value"] >= 0.0
    assert scores["insult"]["value"] >= 0.0