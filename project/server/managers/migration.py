from flask_migrate import Migrate, stamp

from project.server.managers import database


class MigrationManager(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(MigrationManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def init_app(self, app):
        self.migrate = Migrate(app, database.db)

    @staticmethod
    def stamp_db():
        return stamp()
