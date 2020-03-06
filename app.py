from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello workd! from app import app as application'
