from flask import Flask, g
from flask.ext.login import LoginManager
import models

app = Flask(__name__)
app.secret_key = 'fsdfl;jsdkl;v/.xsdlkjlvkxcvleifjsdkjlj234wer90fs'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

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
    models.initialize()
    models.User.create_user(
        name='willowcheng',
        email='e.wingus@gmail.com',
        password='password',
        admin=True
    )
    app.run()
