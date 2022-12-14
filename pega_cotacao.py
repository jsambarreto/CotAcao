from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta 
import matplotlib
import json

from spreedsheet import conecta_drive 

matplotlib.use('SVG')

def pega_cotacao():#arq: str
    today = date.today()
    yesterday = today - timedelta(days=1)
    one_week_ago = today - timedelta(days=7)
    thirty_days_ago = today - timedelta(days=30)

    tabela_empresas = pd.DataFrame(ler_drive())#pd.read_excel(arq)
    cotacaoDiaLista = {}
    for empresa in tabela_empresas['Empresas']:
        cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo',start=thirty_days_ago, end=today) #mes/dia/ano
        cotacaoDia = web.DataReader(f'{empresa}.SA', data_source='yahoo',start=today, end=today) 
        cotacao_dia = cotacaoDia["Adj Close"][0]
        cotacaoDiaLista[f'{empresa}']=float("{:.2f}".format(cotacao_dia))
        normalized_df=(cotacao-cotacao.mean())/cotacao.std()
        normalized_df["Adj Close"].plot(figsize=(10,8), label=empresa, linewidth=4).legend()
    plt.savefig('static/grafico.svg')
    json_object = json.dumps(cotacaoDiaLista, indent = 4) 
    with open("static/data/lista.json", "w") as outfile: 
        outfile.write(json_object)
    outfile.close()
    return cotacaoDiaLista

def ler_json():
    with open('static/data/lista.json', 'r') as openfile:  
        json_object = json.load(openfile)
    return json_object

def ler_drive():
    json_object = conecta_drive()
    return json_object