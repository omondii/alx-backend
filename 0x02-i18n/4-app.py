#!/usr/bin/env python3
""" 4-app.py """
from flask import Flask, request, render_template
from flask_babel import Babel, Locale, gettext as _


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
    if 'locale' in request.json:
        
    best_match = request.accept_languages.best_match(app.Config['LANGUAGES'])
    return Locale.parse(best_match)


@app.route('/')
def index():
    """ Renders the homepage """
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
