from flask import Flask
import models

app = Flask(__name__)

# DEBUG = True
# PORT = 8000
# HOST = '0.0.0.0'

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """"Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
