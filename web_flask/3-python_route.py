#!/usr/bin/python3
""" a script that starts a Flask web application:
        Web application must be listening on 0.0.0.0, port 5000.
        Routes:
            /: display “Hello HBNB!”.
            /hbnb: display “HBNB”.
            /c/<text>: display “C ” followed by the value of the text
            variable (replace underscore _ symbols with a space).
            /python/(<text>): display “Python ”, followed by the value
            of the text variable (replace underscore _ symbols with a space).
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_holbies():
    """
    Displays 'Hello HBNB!'
        Arguments:
            None
        Returns:
            (str)
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_peers():
    """
    Displays 'HBNB'
        Arguments:
            None
        Returns:
            (str)
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_isfun(text):
    """
    Displays 'HBNB'
        Arguments:
            text: variable name
        Returns:
            (str)
    """
    return "C %s" % text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_iscool(text='is cool'):
    """
    Dispalys 'Python'
        Arguments:
            text: variable name
        Returns:
            (str)
    """
    return "Python %s" % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
