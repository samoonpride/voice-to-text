from flask import Flask, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer " + os.getenv("HUGGINGFACE_TOKEN")}

@app.route('/transcribe', methods=['POST'])
def transcribe():
    data = request.files['audio']
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("APP_PORT"))