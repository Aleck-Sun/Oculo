import os
import cv2
import requests
from google.cloud import texttospeech_v1
import pygame

pygame.init()

display_width = 800
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Money Bill Recognition')

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()
crashed = False

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
    
    return fileName

# Comvert image to pygameimage
def convertImage(image):
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1], "RGB")

vid = cv2.VideoCapture(0)
def main():
    # Read frames
    Stopped = False
    while(not Stopped):
        # Capture frame-by-frame
        _, frame = vid.read()
        screen.fill(WHITE)
        
        # Display the resulting frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = convertImage(frame)
        
        screen.blit(image, (0,0))
            
        pygame.display.update()
        clock.tick(60)
        
        # Take a snapshot and send to API
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Stopped = True
            # get mouse pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                f = APIinterfacer("http://localhost:5000/api/classify", frame)
    vid.release()
    pygame.quit()
    
if __name__ == '__main__':
    main()