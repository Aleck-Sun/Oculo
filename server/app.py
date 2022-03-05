import os
import base64
from flask import Flask
from flask import request, send_file
from flask_cors import CORS
from fastai.vision.all import *
from google.cloud import texttospeech_v1

# Load model
model = load_learner('export.pkl')

# Create server
app = Flask(__name__)
CORS(app, supports_credentials=True)

# Setup google cloud text to speech platform
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "serviceAccount.json"
client = texttospeech_v1.TextToSpeechClient()
gender = texttospeech_v1.SsmlVoiceGender.NEUTRAL
voice = texttospeech_v1.VoiceSelectionParams(language_code="en-US", ssml_gender=gender)
audio_config = texttospeech_v1.AudioConfig(audio_encoding=texttospeech_v1.AudioEncoding.MP3)

@app.route("/")
def main():
    return "Server running"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    # Identify image classification
    file = request.json
    classification, _, _ = model.predict(base64.b64decode(file))
    classification = classification.replace("_", "")
    text = classification
    text = texttospeech_v1.SynthesisInput(text=text)

    # Google text-to-speech
    response = client.synthesize_speech(input=text, voice=voice, audio_config=audio_config)
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        out.close()

    # return classification
    return send_file("output.mp3")

if __name__ == "__main__":
    app.run()