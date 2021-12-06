from . import blueprint

from src.util.client import get_data

@blueprint.route('/')
def main():
    data = get_data()
    return data.to_html()