from flask import Blueprint

blueprint = Blueprint('filters', __name__, url_prefix='/filters')

from .amounts import blueprint as amounts
blueprint.register_blueprint(amounts)

from .labs import blueprint as labs
blueprint.register_blueprint(labs)

from .resolutions import blueprint as resolutions
blueprint.register_blueprint(resolutions)

from .states import blueprint as states
blueprint.register_blueprint(states)