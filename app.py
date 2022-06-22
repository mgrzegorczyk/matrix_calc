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
app.secret_key = b'_5#y2L"Fff8z\n\xec[/'

@app.route('/')
def hello():
    #imie = request.args.get("imie", "World")
    #return f'Witaj {escape(imie)}!'
    return render_template("index.html")

@app.route("/podstrona/<imie>")
def nazwa(imie):
    liczby = [1, 2, 3, 4]
    return render_template("podstrona.html", kto=imie, liczby=liczby)


@app.route('/rysunek', methods=['POST', 'GET'])
def rysunek():
    nazwa = None
    liczba = None
    
    rysunek = None
    
    if request.method == 'POST':
        nazwa = request.form["nazwa"]
        plik = request.files["plik"]
        if plik:
            filename = secure_filename(plik.filename)
            path = os.path.join(tempfile.gettempdir(), filename)
            plik.save(path)
        else:
            path = None
        
        if not nazwa:
            nazwa = None
            
            session.pop("nazwa", None)
        else:
            session["nazwa"] = nazwa
        try:
            liczba = int(request.form["liczba"])
            rysunek = rysuj(liczba)
        except ValueError:
            pass
        if path:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        else:
            content = None
        
    else:
        #return redirect(url_for('nazwa', name="Nieznajomy"))
        if "nazwa" in session:
            name = session["nazwa"] + "?"
        else:
            name = "Nieznajomy"
        return redirect(url_for('nazwa', name=name))
    return render_template("rysunek.html", nazwa=nazwa, liczba=liczba,content=content, rysunek=rysunek)

def rysuj(liczba):
    img = io.BytesIO()
    
    plt.plot([0, liczba], [0, liczba], 'r')
    
    plt.savefig(img, format='png')
    img.seek(0)
    url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(url)

