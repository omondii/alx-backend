#!/usr/bin/env python3
""" 3-app.py """
from flask import Flask, render_template
from flask_babel import gettext as _
from flask_babel import Babel


class Config():
    """ Babel config file """
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def index():
    """ Renders the homepage """
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('3-index.html', home_title=home_title, home_header=home_header)

if __name__ == '__main__':
    app.run(debug=True)
