from flask import render_template, request
from werkzeug.utils import redirect

from src.util.forms import get_options

from . import blueprint

from src.util.client import get_data

@blueprint.route('/<num>')
def resolution(num: int):
    data = get_data()
    result = data.query(f'num_resolucion == {num}').to_html()
    return render_template('table.html', table=result, title=f'Resolución')

@blueprint.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        code = request.form['resolution']
        return redirect(f'/filters/resolutions/{code}')
    elif request.method == 'GET':
        options = get_options(get_data(), 'num_resolucion', 'uso_vacuna')
        return render_template('resolutions.html', title='Resoluciones', options=options)
    else:
        return 'Method not allowed'