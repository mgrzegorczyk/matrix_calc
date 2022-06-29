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
from numpy import matrix, linalg



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

@app.route('/podstrona3.html',methods=["POST","GET"])
def stona4():
    if request.method=="POST":
        cell1=request.form["cell1"]
        cell2=request.form["cell2"]
        cell3=request.form["cell3"]
        cell4=request.form["cell4"]
        cell5=request.form["cell5"]
        cell6=request.form["cell6"]
        cell7=request.form["cell7"]
        cell8=request.form["cell8"]
        cell9=request.form["cell9"]

        kom1=request.form["kom1"]
        kom2=request.form["kom2"]
        kom3=request.form["kom3"]
        kom4=request.form["kom4"]
        kom5=request.form["kom5"]
        kom6=request.form["kom6"]
        kom7=request.form["kom7"]
        kom8=request.form["kom8"]
        kom9=request.form["kom9"]
        matrix1= [[cell1,cell2,cell3],[cell4,cell5,cell6],[cell7,cell8,cell9]]
        matrix2=[[kom1,kom2,kom3],[kom4,kom5,kom6],[kom7,kom8,kom9]]
        result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
        for i in range(len(matrix1)):
        # iterate through columns
            for j in range(len(matrix1[0])):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        #return result
        return redirect('stronkatestowa',added=result)
    else:
        return render_template('podstrona3.html')

@app.route("/podstrona3.html?add=Prześlij#")
def stronkatestowa(added):
    return render_template('stronatestowa.html',added=added)