from flask import Blueprint

blueprint = Blueprint(
    'labs',
    __name__,
    url_prefix='/labs',
    template_folder='templates'
)

from . import routes