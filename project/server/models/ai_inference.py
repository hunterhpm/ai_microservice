from project.server.managers.database import db


class Inference(db.Model):
    """ Models Model for storing model related details """
    __tablename__ = "ai_inference"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_on = db.Column(db.DateTime(), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('ai_agent.id'), nullable=True)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    tag = db.Column(db.String(255), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('ai_models.id'), nullable=False)
    camera_id = db.Column(db.Integer, db.ForeignKey('sys_camera.id'), nullable=False)
    dataset = db.Column(db.String(255), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    label = db.Column(db.String(255), nullable=False)


    def __init__(self, updated_on, agent_id, file_name, file_path, tag, model_id, camera_id, dataset, confidence, label):
        self.updated_on = updated_on
        self.agent_id = agent_id
        self.file_name = file_name
        self.file_path = file_path
        self.tag = tag
        self.model_id = model_id
        self.camera_id = camera_id
        self.dataset = dataset
        self.confidence = confidence
        self.label = label

    def from_json(self, json):
        self.id = json.get('inference_id', None)
        self.updated_on = json.get('updated_on', None)
        self.agent_id = json.get('agent_id', None)
        self.file_name = json.get('file_name', None)
        self.file_path = json.get('file_path', None)
        self.tag = json.get('tag', None)
        self.model_id = json.get('model_id', None)
        self.camera_id = json.get('camera_id', None)
        self.dataset = json.get('dataset', None)
        self.confidence = json.get('confidence', None)
        self.label = json.get('label', None)
        return self

    def to_dictionary(self):
        obj = {
            'id': self.id,
            'updated_on': self.updated_on,
            'agent_id': self.agent_id,
            'file_name': self.file_name,
            'file_path': self.file_path,
            'tag': self.tag,
            'model_id': self.model_id,
            'camera_id': self.camera_id,
            'dataset': self.dataset,
            'confidence': self.confidence,
            'label': self.label
        }
        return obj
