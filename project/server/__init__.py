from flask import Flask

from project.server import controllers, decorators
from project.server.config.config import DevelopmentConfig
from project.server.encoders.default_json_encoder import DefaultJSONEncoder
from project.server.managers import auth, bcrypt, cors, database, mail, migration
from project.server.managers.migration import MigrationManager

app = Flask(__name__)
app.json_encoder = DefaultJSONEncoder
app.config.from_object(DevelopmentConfig)

cors.init_app(app)
bcrypt.init_app(app)
database.init_app(app)
auth.init_app(app)
mail.init_app(app)
controllers.init_app(app)
MigrationManager().init_app(app)


