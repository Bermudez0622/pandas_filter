from flask import Blueprint

blueprint = Blueprint('labs', __name__, url_prefix='/labs')

from . import routes