# Application commands

## Running the app

This will start the flask server.

    python app.py runserver

## Testing

This will run the file matching test_*.py in project/tests folder.

    python app.py test
    
## Creating the database

This will initialise the database with default data.

    python app.py create_db
    
## Dropping the database

This will completely drop the database. This needs to be run before create_db.

    python app.py drop_db
    
## Alembic: Migrate

Creates a new migration file. You can then edit the file.

    python app.py db migrate
    
## Alembic: Upgrade

Upgrades the database with the new migrations. You can replace head with a specific revision.

    python app.py db upgrade head
    
## Alembic: Downgrade

Downgrade the database by 1 revision. You can specify the number of revisions.

    python app.py db downgrade
    
    