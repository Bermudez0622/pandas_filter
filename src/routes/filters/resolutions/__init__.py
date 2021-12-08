from flask import Blueprint

blueprint = Blueprint(
    'resolutions',
    __name__,
    url_prefix='/resolutions',
    template_folder='templates'
)

from . import routes