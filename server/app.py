from flask import Flask
from flask import request
from flask_cors import CORS
from fastai.vision.all import *
import base64

import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

# Load model
model = load_learner('export.pkl')

# Create server
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def main():
    return "Server Running"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    # Identify image classification
    #file = request.files['file']
    
    
    
    #print(file)
    #classification, _, probability = model.predict(file)
    #print("Bill:", classification, "Confidence", probability)

    #classification = classification.replace("_", "")
    #return classification
