#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
from flask import Flask
=======
"""This script starts the Flask web application"""
from flask import Flask

>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
<<<<<<< HEAD
    """Handles the root url"""
=======
    """
    Returns a string
    """
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Handles hbnb route"""
=======
    """
    Returns a string
    """
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
<<<<<<< HEAD
    """Handles /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Handles /python/<text> route"""
=======
    """
    Returns C followed by the value of the text variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    displays "Python" followed by a text
    """
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
<<<<<<< HEAD
    app.run("0.0.0.0", 5000)
=======
    """
    Ensures that the module is not executable when  imported
    """
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
