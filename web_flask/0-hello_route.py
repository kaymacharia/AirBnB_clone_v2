#!/usr/bin/python3
<<<<<<< HEAD
"""Module - the script that starts a Flask web application"""
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


if __name__ == '__main__':
<<<<<<< HEAD
    app.run("0.0.0.0", 5000)
=======
    """
    Ensures that the module is not executable when  imported
    """
    app.run(host='0.0.0.0', port=5000)
>>>>>>> e7fb1f87cc1e4afe39b67ba1c46372a9aabb2bbd
