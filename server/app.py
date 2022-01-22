import os
from flask import Flask
from flask import request
from flask_cors import CORS
from google.cloud import texttospeech_v1

# Setup google cloud text to speech platform
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "serviceAccount.json"
client = texttospeech_v1.TextToSpeechClient()
gender = texttospeech_v1.SsmlVoiceGender.NEUTRAL
voice = texttospeech_v1.VoiceSelectionParams(Language_code="en-US", ssml_gender=gender)
audio_config = texttospeech_v1.AudioConfig(audio_encoding=texttospeech_v1.AudioEncoding.MP3)

# Create server
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def main():
    return "Server Running"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    # Grab image file from request
    print(request.files['file'].filename)

    # Identify image classification (TODO)
    text = "five dollar bill"

    # Synthesize input and save as mp3
    text = "five dollar bill"
    text = texttospeech_v1.SynthesisInput(text=text)
    response = client.synthesize_speech(input=text, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        
    return "Hi for now"