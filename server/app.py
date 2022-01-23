from flask import Flask
from flask import request
from flask_cors import CORS
from fastai.vision.all import *

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
    # Grab image file from request
    print(request.files['file'].filename)

    # Identify image classification
    classification, _, probability = model.predict(files['file'])
    print("Bill:", classification, "Confidence", probability)

    # Check to see if model is confident
    text = "Unknown bill amount, please rescan"
    if probability > 0.7:
        text = classification

    return text