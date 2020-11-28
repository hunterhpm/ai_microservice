from flask import make_response, jsonify
from project.server.controllers.v1 import errors
from project.server.managers.database import db

from project.server.models.ai_models import Models
from project.server.helpers.serialize import get_json_clean_response
from datetime import datetime
from sqlalchemy import and_
import logging


def select_all_models():
    query = get_json_clean_response(Models.query.all())
    # inferences = query.model.all()
    # inferences = get_json_clean_response(ai_agent.query.all())
    response_object = {
        'status': 'success',
        'data': query
    }
    return make_response(jsonify(response_object)), 200