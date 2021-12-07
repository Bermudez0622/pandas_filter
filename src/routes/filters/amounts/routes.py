from flask import render_template

from . import blueprint

from src.util.client import get_data

@blueprint.route('/<filter>')
def amount(filter: str):
    data = get_data()
    result = data.query(f'cantidad {filter}').to_html(classes='table')
    return render_template('table.html', table=result, title='Cantidad de vacunas')

@blueprint.route('/form')
def form():
    return render_template('table.html', title='Cantidad de vacunas aplicadas')