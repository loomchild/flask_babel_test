#!/usr/bin/env python
from flask import Flask, request
from flask.ext.babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

#@babel.localeselector
#def get_locale():
#    translations = [str(translation) for translation in babel.list_translations()]
#    return request.accept_languages.best_match(translations)

@app.route("/")
def index():
    return gettext("Hello world")


if __name__ == '__main__':
    app.run(debug=True)
