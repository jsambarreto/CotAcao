#from aioflask import Flask, render_template
from flask import Flask,jsonify, render_template
from pega_cotacao import ler_drive, ler_json, pega_cotacao

app = Flask(__name__)

@app.route('/')
def api_cotacao(lista=None):
    lista = pega_cotacao()
    return jsonify(lista)

@app.route('/grafico')
def grafico():
    return render_template('index.html')

@app.route('/lista')
def lista(lista=None):
    lista = ler_json()
    return render_template('index.html', lista = lista)

@app.route('/new_lista')
def newLista(lista=None):
    lista = ler_drive()
    return jsonify(lista)#render_template('index.html', lista = lista)