from flask import Blueprint

blueprint = Blueprint(
    'amounts',
    __name__,
    url_prefix='/amounts',
    template_folder='templates',
)

from . import routes