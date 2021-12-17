#!/usr/bin/python3
"""
starts a Flask web application
"""

if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage, State, Amenity

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/hbnb_filters')
    def hbnb_filters():
        """
        sets the route for '/hbnb_filters'
        """
        return render_template('10-hbnb_filters.html',
                               states=storage.all(State),
                               amenities=storage.all(Amenity))

    @app.teardown_appcontext
    def teardown(context):
        """
        resets storage after each request
        """
        storage.close()

    app.run(host='0.0.0.0', port='5000')
