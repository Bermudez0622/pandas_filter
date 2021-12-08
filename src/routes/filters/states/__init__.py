from flask import Blueprint

blueprint = Blueprint(
    'states',
    __name__,
    url_prefix='/states',
    template_folder='templates'
)

from . import routes