#!/bin/python

from flask import Flask
from pandas import DataFrame, to_numeric
from sodapy import Socrata

from os import getenv

client = Socrata(getenv("SOURCE_HOST"), None)

def get_data():
    results = client.get(getenv("SOURCE_FILE"))
    data_frame = DataFrame.from_records(results)
    data_frame['num_resolucion'] = to_numeric(data_frame['num_resolucion'])
    data_frame['cod_territorio'] = to_numeric(data_frame['cod_territorio'])
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
def resolution(num: int):
    data = get_data()
    return data.query(f'num_resolucion == {num}').to_html()

@app.route('/state/<code>')
def territory(code: int):
    data = get_data()
    return data.query(f'cod_territorio == {code}').to_html()

@app.route('/amount/<filter>')
def amount(filter: str):
    data = get_data()
    return data.query(f'cantidad {filter}').to_html()

if __name__ == '__main__':
    app.run()