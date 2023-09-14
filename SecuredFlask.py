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

'''
Added Headers :
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'self'
Referrer-Policy: strict-origin-when-cross-origin
'''
'''
You can also use the @talisman decorator 
to gain more control over security at the route level if needed.
'''
'''
Talisman also ensures that your domain uses HTTPS instead of HTTP
'''