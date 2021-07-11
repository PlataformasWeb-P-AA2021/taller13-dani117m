from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificio")
def los_edificio():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/",
            auth=('dani', '123'))
    edificio = json.loads(r.content)['results']
    numero_edificio = json.loads(r.content)['count']
    return render_template("losedificio.html", edificio=edificio,
    numero_edificio=numero_edificio)


@app.route("/losdepartamento")
def los_departamento():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('dani', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamento.html", datos=datos,
    numero=numero)


@app.route("/losdepartamento")
def los_departamento_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('dani', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_completo':d['nombre_completo'], 'num_cuartos':d['num_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentodos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('dani', '123'))
    nombre_edificio = json.loads(r.content)['nombre'], json.loads(r.content)['direccion'],
    json.loads(r.content)['ciudad'],json.loads(r.content)['tipo']
    return nombre_edificio
