from flask import Blueprint

blueprint = Blueprint('amounts', __name__, url_prefix='/amounts')

from . import routes