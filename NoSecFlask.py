# This application simply sends back a static HTML page called index.html from the root / URL.

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Base URL for our service"""
    return app.send_static_file("index.html")
