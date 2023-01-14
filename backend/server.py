from flask import Flask
import cohere

co = cohere.Client("0QhbB7ejcdwWnfaO38OHpWkgi7pdPR5x7AqGpSl9")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'