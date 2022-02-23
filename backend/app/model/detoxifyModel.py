from flask import jsonify
from detoxify import Detoxify
import pandas as pd

def toxicity_check(sentence): 
    results = Detoxify('original').predict(sentence)
    df = pd.DataFrame(results, index=["value"]).round(2)
    json = df.to_json()
    return json