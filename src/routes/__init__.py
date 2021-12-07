from flask import Blueprint

blueprint = Blueprint(
    'routes',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from .main import blueprint as main
blueprint.register_blueprint(main)

from .filters import blueprint as filters
blueprint.register_blueprint(filters)