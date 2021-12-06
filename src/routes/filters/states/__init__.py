from flask import Blueprint

blueprint = Blueprint('states', __name__, url_prefix='/states')

from . import routes