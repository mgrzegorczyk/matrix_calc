#from flask import Flask, escape, request
from importlib.resources import contents
from flask import Flask, render_template

from flask import request, redirect, url_for

from werkzeug.utils import secure_filename
import os
import tempfile

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from flask import session


#from flask import Response


app = Flask(__name__)
app.secret_key = b'\xf0xK\xd7\x07\\r\xf3^\x8f'

@app.route('/')
def strona1():
    return render_template('stronaglowna.html')

@app.route('/podstrona1.html')
def strona2():
    return render_template('podstrona1.html')

@app.route('/podstrona2.html')
def stona3():
    return render_template('podstrona2.html')

@app.route('/podstrona3.html')
def stona4():
    return render_template('podstrona3.html')