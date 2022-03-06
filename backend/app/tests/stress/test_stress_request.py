import pytest
import requests
import time

# 100 REQUEST PER MINUTE
request_number_limit = 100
request_time_limit = 60

def test_response():
    interval = 60 / 100
    single_request_duration = request_number_limit / request_time_limit
    for request in range(50):
        assert requests.get('http://127.0.0.1:5000/api/toxicity?sentence=TEST').status_code == 200
        assert requests.get('http://127.0.0.1:5000/api/toxicity?sentence=TEST').elapsed.total_seconds() < single_request_duration
        time.sleep(interval)