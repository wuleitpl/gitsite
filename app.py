from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello world! from app import app as application'
