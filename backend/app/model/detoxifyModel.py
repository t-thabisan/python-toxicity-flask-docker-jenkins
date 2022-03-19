from flask import jsonify
from detoxify import Detoxify
import pandas as pd

toxicity_model = Detoxify('original')

def toxicity_check(sentence): 
    results = toxicity_model.predict(sentence)
    df = pd.DataFrame(results, index=["value"]).round(2)
    json = df.to_json()
    return json