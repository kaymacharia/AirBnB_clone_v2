#!/usr/bin/python3
<<<<<<< HEAD
"""Module - script that starts a Flask web application"""
from flask import Flask, render_template
=======
"""This script starts the Flask web application"""
from flask import Flask
from flask import render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
<<<<<<< HEAD
    """Handles /number/<n> route"""
=======
    """
    Displays "n is a number" only if n is an interger
    """
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
<<<<<<< HEAD
    """Handles /number_template/<int:n> route"""
=======
    """
    Displays a HTML page only if n is an integer
    """
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
<<<<<<< HEAD
    """Handles /number_template/<int:n> route"""
    parity = 'odd'
    if n % 2 == 0:
        parity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
=======
    """
    displays a HTML epage only if n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """
    Ensures that the module is not executable when  imported
    """
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
