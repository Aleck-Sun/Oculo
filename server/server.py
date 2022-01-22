from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route("/")
def main():
    return "Server Running"

@app.route("/api/v0/classifyImage", methods=['POST'])
def classifyImage():
    print(request)
    return "We return the dollar bill here"