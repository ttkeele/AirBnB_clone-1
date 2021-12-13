#!/usr/bin/python3
"""Starts a Flask app"""


if __name__ == '__main__':
    from flask import Flask

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/')
    def hello():
        """
        sets the route for '/'
        """
        return "Hello HBNB!"

    app.run(host='0.0.0.0', port='5000')
