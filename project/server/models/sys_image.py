from datetime import datetime
from project.server.managers.database import db


class Image(db.Model):
    """ Image Model for storing image related details """
    __tablename__ = 'sys_image'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    updated_on = db.Column(db.DateTime, nullable=True, default=datetime.now())
    image_path = db.Column(db.String(255), nullable=False)
    camera_id = db.Column(db.String(255), nullable=False)

    def __init__(self, updated_on, image_path, ai_agent, camera_id):
        self.updated_on = updated_on
        self.image_path = image_path
        self.ai_agent = ai_agent
        self.camera_id = camera_id

    def from_json(self, json):
        self.id = json.get('image_id', None)
        self.updated_on = json.get('updated_on', None)
        self.image_path = json.get('image_path', None)
        self.ai_agent = json.get('ai_agent', None)
        self.camera_id = json.get('camera_id', None)
        return self

    def to_dictionary(self):
        obj = {
            'image_id': self.image_id,
            'updated_on': self.updated_on,
            'image_path': self.image_path,
            'ai_agent': self.ai_agent,
            'camera_id': self.camera_id,
        }
        return obj
