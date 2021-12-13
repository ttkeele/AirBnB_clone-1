#!/usr/bin/python3
"""Starts a Flask app"""

if __name__ == '__main__':
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    """
    sets the route for '/'
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb_route():
    """
    route for '/hbnb'
    """
    return "HBNB"

@app.route('/c/<text>')
def c_route(text):
    """
    routes /c/<text> to display 'C <text>'
    replaces '_' in <text> with ' '
    """
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text="is cool"):
    """
    routes /python/<text> to display 'Python <text>'
    replaces '_' in <text> with ' '
    <text> defaults to 'is cool'
    """
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number_route(n):
    """
    displays '<n> is a number'
    only accepts integers
    """
    return "{} is a number".format(n)

 @app.route('/number_template/<int:n>')
 def number_template(n):
     """
     displays number using a template
     """
     return render_template('5-number.html', n=n)

 app.run(host='0.0.0.0', port='5000')
