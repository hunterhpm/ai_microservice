from flask import make_response, jsonify
from project.server.controllers.v1 import errors
from project.server.managers.database import db

from project.server.models.sys_image import Image
from project.server.helpers.serialize import get_json_clean_response
from datetime import datetime
from sqlalchemy import and_
import logging


def next_inference(inference_object, ai_manager_object):
    json_response = jsonify(inference_object)
    logging.info("Hello")
    try:

        inference = Image(
            timestamp=datetime.now(),
            formated_time=datetime.now(),
            cpu=ai_manager_object.get('CPU'),
            ram=ai_manager_object.get('RAM'),
            image_size='sfh',
            spot_name='dfjhj',
            thresold=1.2,
            weight_file='dfj',
            big_label=True,
            big_status="active",
            base64="NULL",
            batch_result=True,
            camera_ID=inference_object.get('camera_ID'),
            confidence=inference_object.get('confidence'),
            filename=inference_object.get('filename'),
            label=inference_object.get('label'),
            orientation=inference_object.get('orientation')
        )
        db.session.add(inference)
        db.session.commit()
        return make_response(jsonify(str(inference_object))), 200
    except Exception as e:
        errors.unauthorized(e)

    return make_response(jsonify(str(inference_object))), 200


def select_all_inference():
    inferences = get_json_clean_response(Image.query.all())
    response_object = {
        'status': 'success',
        'data': inferences
    }
    return make_response(jsonify(response_object)), 200


def calendar(start_date, end_date):
    inferences = get_json_clean_response(Image.query.filter(
        and_(Image.timestamp >= datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S'),
             Image.timestamp <= datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S'))).all())

    response_object = {
        'status': 'success',
        'data': inferences
    }
    return make_response(jsonify(response_object)), 200
