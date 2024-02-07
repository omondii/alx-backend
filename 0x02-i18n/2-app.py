#!/usr/bin/env python3
""" 2-app.py """
from flask import Flask, request, render_template
from flask_babel import Babel, Locale


class Config():
    """ Babel configuration file """
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determines the best match with our supported languages. """
    best_match = request.accept_languages.best_match(app.Config['LANGUAGES'])
    return Locale.parse(best_match)


@app.route('/')
def index():
    """ A route that renders an html template """
    locale = get_locale()
    return render_template('2-index.html', locale=locale)


if __name__ == "__main__":
    app.run(debug=True)
