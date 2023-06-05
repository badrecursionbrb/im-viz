from flask_app import flask_app

import os
os.environ["PATH"] += os.pathsep + '/usr/bin/'
# this is the file for hosting the gunicorn app named 'gunicorn_app'

if __name__ == "__main__":
    flask_app.run()