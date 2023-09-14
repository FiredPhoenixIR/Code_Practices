# This version of the application uses Flask-Talisman to add security headers 
# that reject loading content from other sites, making your application more secure.

from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
# Create a content security policy and apply it
csp = {
    'default-src': '\'self\''
}
talisman = Talisman(app, content_security_policy=csp)

@app.route('/', methods=['GET'])
def index():
    """Base URL for our service"""
    return app.send_static_file("index.html")
