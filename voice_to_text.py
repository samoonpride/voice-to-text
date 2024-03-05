from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os
import asyncio

load_dotenv()

app = Flask(__name__)
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
HEADERS = {"Authorization": "Bearer " + os.getenv("HUGGINGFACE_TOKEN")}


async def perform_inference(audio_data):
    try:
        response = requests.post(API_URL, headers=HEADERS, data=audio_data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}


@app.route('/transcribe', methods=['POST'])
def transcribe():
    try:
        audio_file = request.files['audio']
        audio_data = audio_file.read()
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(perform_inference(audio_data))
        return jsonify(result)
    except KeyError:
        return jsonify({"error": "No audio file provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("APP_PORT"))
