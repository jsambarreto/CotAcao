#from aioflask import Flask, render_template
from flask import Flask,jsonify, render_template
from pega_cotacao import pega_cotacao

app = Flask(__name__)

@app.route('/')
def api_cotacao(lista=None):
    lista = pega_cotacao("Empresas.xlsx")
    return jsonify(lista)

@app.route('/grafico')
def grafico():
    return render_template('index.html')