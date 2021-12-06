from . import blueprint

from src.util.client import get_data

@blueprint.route('/<num>')
def resolution(num: int):
    data = get_data()
    return data.query(f'num_resolucion == {num}').to_html()

@blueprint.route('/form')
def form():
    return {"Form": "Resolution"}