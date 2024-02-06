#!/usr/bin/env python3
""" 1-app.py """
from flask import Flask
from flask_babel import Babel


class Config:
    """ Babel Configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


