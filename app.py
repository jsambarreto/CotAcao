#from aioflask import Flask, render_template
from flask import Flask,jsonify
from pega_cotacao import pega_cotacao

app = Flask(__name__)

@app.route('/')
def hello(lista=None):
    lista = pega_cotacao("Empresas.xlsx")
    return jsonify(lista)