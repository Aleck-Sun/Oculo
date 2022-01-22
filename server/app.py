from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def main():
    return "Server Running"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    print(request.data)
    return "We return the dollar bill here"