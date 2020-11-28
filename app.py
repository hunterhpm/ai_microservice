import glob
import os
import unittest

import coverage


from flask import jsonify
from flask_fixtures import load_fixtures

from flask_fixtures.loaders import JSONLoader
from flask_script import Manager
from flask_migrate import MigrateCommand

from project.server import app, MigrationManager
from project.server.config import config
from project.server.managers import database
from project.server.managers.schema import get_ulm

manager = Manager(app)
# migrations
manager.add_command('db', MigrateCommand)


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/server/config.py',
        'project/server/*/__init__.py'
    ]
)
COV.start()



@app.route('/start_GPU')
def GPU_startup():
    return jsonify("GPU VM is start in 5 minutes")


@app.route('/stop_GPU')
def GPU_stop():
    return jsonify("GPU VM is stop")

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1


@manager.command
def create_db():
    """Creates the db tables."""
    database.db.create_all()
    get_ulm()
    for fixture_file in glob.glob(config.DevelopmentConfig.FIXTURES_DIRS + '/*.json'):
        fixtures = JSONLoader().load(fixture_file)
        load_fixtures(database.db, fixtures)
        MigrationManager().stamp_db()


@manager.command
def drop_db():
    """Drops the db tables."""
    database.db.reflect()
    database.db.drop_all()
    print('Dropped the database')


if __name__ == "__main__":
    manager.run()
