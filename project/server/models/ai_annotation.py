import datetime

from project.server.helpers.encrypter import encrypt_password
from project.server.managers.database import db


class Annotation(db.Model):
    """ Models Model for storing model related details """
    __tablename__ = "ai_annotation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_on = db.Column(db.DateTime(), nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey('ai_image_attribute.id'), unique=True, nullable=False)
    category_id = db.Column(db.String(255), unique=True, nullable=False)
    segmentation = db.Column(db.String(255), unique=True, nullable=False)
    bbox = db.Column(db.String(255), unique=True, nullable=False)
    ignore = db.Column(db.Boolean, unique=True, nullable=False)
    iscrowd = db.Column(db.Boolean, unique=True, nullable=False)
    area = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, updated_on, image_id, category_id, segmentation, bbox, ignore, iscrowd, area):
        self.updated_on = updated_on
        self.image_id = image_id
        self.category_id = category_id
        self.segmentation = segmentation
        self.bbox = bbox
        self.ignore = ignore
        self.iscrowd = iscrowd
        self.area = area

    def from_json(self, json):
        self.id = json.get('user_id', None)
        self.updated_on = json.get('updated_on', None)
        self.image_id = json.get('image_id', None)
        self.category_id = json.get('category_id', None)
        self.segmentation = json.get('segmentation', None)
        self.bbox = json.get('bbox', None)
        self.ignore = json.get('ignore', None)
        self.iscrowd = json.get('iscrowd', None)
        self.area = json.get('area', None)
        return self

    def to_dictionary(self):
        obj = {
            'annotation_id': self.id,
            'updated_on': self.updated_on,
            'image_id': self.image_id,
            'category_id': self.category_id,
            'segmentation': self.segmentation,
            'bbox': self.bbox,
            'ignore': self.ignore,
            'iscrowd': self.iscrowd,
            'area': self.area
        }
        return obj