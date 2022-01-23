from flask import Flask
from flask import request
from flask_cors import CORS
from fastai.vision.all import *
import base64
import json
from PIL import Image
from io import BytesIO

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
    return "Server Running v 1.2"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    #Identify image classification
    data = json.loads(request.data.decode("ascii"))['file']
    classification, _, probability = model.predict(base64.b64decode(data[22:]))
    print("Bill:", classification, "Confidence", probability)

    classification = classification.replace("_", "")
    return classification
