import sys
from flask import request, jsonify
from model.detoxifyModel import toxicity_check
#from prometheus_client import Counter



default_string = 'To check a sentence toxicity, call : http://localhost:5000/api/toxicity?sentence=YourSentence'

undefined_string = 'no sentence'

#REQUESTS = Counter('toxicity_sentence_check_total', 'toxicity sentence check requested.')

def default():
    return default_string
    
def toxicity_sentence_check():
    sentence = request.args.get('sentence')
    
    # Empty sentence
    if sentence is None:
        sentence = undefined_string
        
    # Call Toxicity Model
    result = toxicity_check(sentence)
    #REQUESTS.inc() 
    return result