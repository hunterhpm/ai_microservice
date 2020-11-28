from project.server.handlers.database.models import select_all_models

def get_models():
    return select_all_models()