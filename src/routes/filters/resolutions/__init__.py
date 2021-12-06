from flask import Blueprint

blueprint = Blueprint('resolutions', __name__, url_prefix='/resolutions')

from . import routes