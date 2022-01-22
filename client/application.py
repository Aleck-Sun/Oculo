import os
import cv2
import requests
from google.cloud import texttospeech_v1

# Setup google cloud text to speech platform
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "serviceAccount.json"
client = texttospeech_v1.TextToSpeechClient()
gender = texttospeech_v1.SsmlVoiceGender.NEUTRAL
voice = texttospeech_v1.VoiceSelectionParams(language_code="en-US", ssml_gender=gender)
audio_config = texttospeech_v1.AudioConfig(audio_encoding=texttospeech_v1.AudioEncoding.MP3)

def APIinterfacer(url, blob : bytes) -> str:
    files = { 'file': ("moneyBill.jpg", blob), 'Content-Type': 'image/jpeg', 'Content-Length': 1 }
    
    # Get classification from server
    response = requests.post(url, files=files)
    text = response.text

    # Get audio file from google cloud
    text = texttospeech_v1.SynthesisInput(text=text)
    response = client.synthesize_speech(input=text, voice=voice, audio_config=audio_config)
    audio = response.audio_content
    fileName = "classification.mp3"

    # Save speech
    with open(fileName, "wb") as out:
        out.write(audio)
    
    # Play the audio here and wait until it's done playing (TODO)
    
vid = cv2.VideoCapture(0)
def main():
    # Read frames
    while(True):
        _, frame = vid.read()
        cv2.imshow('frame', frame)
        
        # Take a snapshot and send to API
        if cv2.waitKey(1) & 0xFF == ord('q'):
            _, buffer = cv2.imencode('.jpg', frame)
            APIinterfacer("http://localhost:5000/api/v0/classifyImage", buffer)
            break
        
        
    vid.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()