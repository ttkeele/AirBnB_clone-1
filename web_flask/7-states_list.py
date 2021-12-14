#!/usr/bin/python3
"""Starts a Flask app"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states_list')
def states_list():
    """
    sets the route for '/states_list'
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(context):
    """resets storage after each request"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
