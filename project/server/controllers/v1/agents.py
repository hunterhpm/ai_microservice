from flask_jwt_extended import jwt_required

from project.server.decorators.authentification import admin_required
from project.server.handlers.database.agents import select_all_agents

def get_all_agents():
    return select_all_agents()