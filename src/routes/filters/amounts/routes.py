from flask import render_template, request, redirect

from src.util.client import get_data

from . import blueprint


@blueprint.route('/<filter>')
def amount(filter: str):
    data = get_data()
    result = data.query(f'cantidad {filter}').to_html()
    return render_template('table.html', table=result, title='Cantidad de vacunas')

@blueprint.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        operation = request.form['operation']
        value = request.form['value']
        return redirect(f'/filters/amounts/{operation} {value}')
    elif request.method == 'GET':
        return render_template('amounts.html', title='Cantidad de vacunas')
    else:
        return 'Method not allowed'