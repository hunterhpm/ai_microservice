from flask_jwt_extended import jwt_required
from flask import request, make_response, jsonify
#fom project.server.handlers.database.monitoring import next_inference, calendar, select_all_inference
#from project.server.inference.inference_result import *
import tensorflow as tf
import json

AUTOTUNE = tf.data.experimental.AUTOTUNE
CONFIG_FILE = 'config_SC.json'
MEM_PER_MODEL = 10000

with open(CONFIG_FILE) as f:
    config = json.load(f)
CONFIG_DICT = config['InferenceDetails']
DATA_DIR = config['DATA_DIR']
CAMERA_LIST = list(CONFIG_DICT.keys())
print("Found {} Cameras in {}".format(len(CAMERA_LIST), CONFIG_FILE))
print("List of Cameras : ", CAMERA_LIST)

def inference():
    return "H"
    
def get_all_inference():
    return "Hi"
    
def get_calendar():
    return "Hello world"

