from . import blueprint

from src.util.client import get_data

@blueprint.route('/<filter>')
def amount(filter: str):
    data = get_data()
    return data.query(f'cantidad {filter}').to_html()

@blueprint.route('/form')
def form():
    return {"Form": "Amount"}