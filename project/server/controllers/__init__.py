import sys

from flask.blueprints import Blueprint

from project.server.config import routes


def init_app(app):
    for version in routes.ROUTES:
        blueprint = Blueprint(version, __name__)
        module = 'project.server.controllers.%s.' % version

        for route in routes.ROUTES[version]:
            endpoint = route.get('endpoint')
            function = route.get('function')
            method = route.get('method')
            rule = route.get('rule')
            __import__(module + endpoint, fromlist=[''])
            blueprint.add_url_rule(
                rule,
                endpoint=endpoint + ' ' + function,
                view_func=getattr(sys.modules[module + endpoint], function),
                methods=[method],
                strict_slashes=False
            )
        app.register_blueprint(blueprint, url_prefix='/' + version)
