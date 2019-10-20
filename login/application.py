from __future__ import print_function
from flask import Flask, render_template, url_for, redirect, request
from flask_caching import Cache
from flask_restful import Api
import secrets
secret = secrets.token_hex(16)

application = app = Flask(__name__)
api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return ('Hello world!')
    return render_template('login.html', error=error)

if __name__=='__main__':
    app.run(debug=True)