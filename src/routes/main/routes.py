from flask.templating import render_template
from . import blueprint

from src.util.client import get_data

@blueprint.route('/')
def main():
    data = get_data()
    result = data.to_html()
    return render_template('index.html', table=result, title='Tabla sin filtros')

@blueprint.route('/table')
def table():
    data = get_data()
    result = data.to_html()
    return render_template('table.html', table=result, title='Tabla sin filtros')