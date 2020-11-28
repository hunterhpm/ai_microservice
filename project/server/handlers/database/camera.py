from flask import make_response, jsonify
from project.server.controllers.v1 import errors
from project.server.managers.database import db

from project.server.models.sys_camera import Camera
from project.server.helpers.serialize import get_json_clean_response
from datetime import datetime
from sqlalchemy import and_
import logging


def insert_preset():
    return "df"