from flask import render_template

from . import blueprint

from src.util.client import get_data

@blueprint.route('/<code>')
def territory(code: int):
    data = get_data()
    return data.query(f'cod_territorio == {code}').to_html()

@blueprint.route('/form')
def form():
    return render_template('tables.html', title='Territorios')