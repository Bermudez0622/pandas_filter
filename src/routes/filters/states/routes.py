from flask import render_template, redirect, request

from src.util.forms import get_options

from . import blueprint

from src.util.client import get_data

@blueprint.route('/<code>')
def territory(code: int):
    data = get_data()
    result = data.query(f'cod_territorio == {code}').to_html()
    return render_template('table.html', table=result, title=f'Territorio')

@blueprint.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        code = request.form['state']
        return redirect(f'/filters/states/{code}')
    elif request.method == 'GET':
        options = get_options(get_data(), 'cod_territorio', 'nom_territorio')
        return render_template('states.html', title='Territorios', options=options)
    else:
        return 'Method not allowed'