from flask.templating import render_template

from . import blueprint

from src.util.client import get_data

@blueprint.route('/<name>')
def lab(name: str):
    data = get_data()
    return data[data['laboratorio_vacuna'].str.contains(name.upper())].to_html()

@blueprint.route('/form')
def form():
    return render_template('table.html', title='Laboratorios')