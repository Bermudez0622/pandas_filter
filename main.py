#!/bin/python

from flask import Flask, request
from numpy import number
from pandas import DataFrame, to_numeric
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None)

def get_data():
    results = client.get("sdvb-4x4j")
    data_frame = DataFrame.from_records(results)
    data_frame['cantidad'] = to_numeric(data_frame['cantidad'])
    return data_frame

app = Flask(__name__)

@app.route('/')
def main():
    data = get_data()
    return data.to_html()

@app.route('/lab/<name>')
def lab(name: str):
    data = get_data()
    return data[data['laboratorio_vacuna'].str.contains(name.upper())].to_html()

@app.route('/resolution/<num>')
def resolution(num: number):
    data = get_data()
    return data.query(f'num_resolucion == {num}').to_html()

@app.route('/state/<code>')
def territory(code: number):
    data = get_data()
    return data.query(f'cod_territorio == {code}').to_html()

@app.route('/amount/<filter>')
def amount(filter: number):
    data = get_data()
    return data.query(f'cantidad {filter}').to_html()

if __name__ == '__main__':
    app.run()