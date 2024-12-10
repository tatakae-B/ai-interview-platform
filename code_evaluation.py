import requests

def evaluate_code(source_code, language_id, input_data=""):
    url = "https://api.judge0.com/submissions/?base64_encoded=false&wait=true"
    headers = {"Content-Type": "application/json"}
    data = {
        "source_code": source_code,
        "language_id": language_id,
        "stdin": input_data
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()
