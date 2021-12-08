from flask import render_template, request, redirect

from . import blueprint

from src.util.client import get_data
from src.util.forms import get_options

@blueprint.route('/<name>')
def lab(name: str):
    data = get_data()
    result = data[data['laboratorio_vacuna'].str.contains(name.upper())].to_html()
    return render_template('table.html', table=result, title='Laboratorio de vacunas')

@blueprint.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        code = request.form['lab']
        return redirect(f'/filters/labs/{code}')
    elif request.method == 'GET':
        options = get_options(get_data(), 'laboratorio_vacuna')
        return render_template('labs.html', title='Laboratorios', options=options)
    else:
        return 'Method not allowed'