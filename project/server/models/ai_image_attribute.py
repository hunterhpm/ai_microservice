from project.server.managers.database import db
from project.server.models.sys_camera import ai_agent


class Image_Attribute(db.Model):
    """ Models Model for storing model related details """
    __tablename__ = "ai_image_attribute"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_on = db.Column(db.DateTime(), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('ai_agent.id'), unique=True, nullable=False)
    file_name = db.Column(db.String(255), unique=True, nullable=False)
    file_path = db.Column(db.String(255), unique=True, nullable=False)
    tag_id = db.Column(db.String(255), unique=True, nullable=False)
    model_id = db.Column(db.String(255), unique=True, nullable=False)
    model_output = db.Column(db.String(255), unique=True, nullable=False)
    dataset = db.Column(db.String(255), nullable=False)
    annotation_path = db.Column(db.String(255), nullable=False)
    flagging = db.Column(db.String(255), nullable=False)
    image_attributes = db.Column(db.String(255), nullable=False)
    license = db.Column(db.String(255), nullable=False)
    width = db.Column(db.Float , nullable=False)
    height = db.Column(db.Float, nullable=False)


    def __init__(self, updated_on, agent_id, image_id, tag_id, model_id, model_output, dataset, annotation_path, flagging, width):
        self.updated_on = updated_on
        self.agent_id = agent_id
        self.image_id = image_id
        self.tag_id = tag_id
        self.model_id = model_id
        self.model_out = model_output
        self.dataset = dataset
        self.annotation_path = annotation_path
        self.flagging = flagging
        self.width = width

    def from_json(self, json):
        self.id = json.get('id', None)
        self.updated_on = json.get('updated_on', None)
        self.agent_id = json.get('agent_id', None)
        self.image_id = json.get('image_id', None)
        self.tag_id = json.get('tag_id', None)
        self.model_id = json.get('model_id', None)
        self.model_output = json.get('model_output', None)
        self.dataset = json.get('dataset', None)
        self.annotation_path = json.get('annotation_path', None)
        self.flagging = json.get('flagging', None)
        return self

    def to_dictionary(self):
        obj = {
            'id': self.id,
            'updated_on': self.updated_on,
            'agent_id': self.agent_id,
            'image_id': self.image_id,
            'tag_id': self.tag_id,
            'model_id': self.model_id,
            'model_output': self.model_output,
            'dataset': self.dataset,
            'annotation_path': self.annotation_path,
            'flagging': self.flagging
        }
        return obj
