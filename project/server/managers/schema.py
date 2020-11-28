import codecs
import sadisplay
# from project.server.models.auth_user import User

from project.server import models


def get_ulm():
    desc = sadisplay.describe(
        [getattr(models, attr) for attr in dir(models)],
        show_methods=True,
        show_properties=True,
        show_indexes=True,
    )
    with codecs.open('doc/database/schema.plantuml', 'w', encoding='utf-8') as f:
        f.write(sadisplay.plantuml(desc))
    with codecs.open('doc/database/schema.dot', 'w', encoding='utf-8') as f:
        f.write(sadisplay.dot(desc))
