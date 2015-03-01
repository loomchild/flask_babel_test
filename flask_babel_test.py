#!/usr/bin/env python
from flask import Flask
from flask.ext.babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

@app.route("/")
def index():
    return gettext("Hello world")


if __name__ == '__main__':
    app.run(debug=True)
