from flask import Flask
from flask import request
from flask import send_file
from flask_cors import CORS

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
    text = "twenty dollar bill"
    return text