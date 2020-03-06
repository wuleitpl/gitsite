
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world! Hello from Flask! This is the first web app built by wulei. Edit on dell! Edit on site!'
