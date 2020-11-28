from project.server.managers.database import db


class Tag(db.Model):
    """ Models Model for storing model related details """
    __tablename__ = "ai_tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    updated_on = db.Column(db.DateTime(), nullable=False)
    tag_name = db.Column(db.String(255), unique=True, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('ai_agent.id'),  nullable=False)

    def __init__(self, updated_on, tag_name, value, description, agent_id):
        self.updated_on = updated_on
        self.tag_name = tag_name
        self.value = value
        self.description = description
        self.agent_id = agent_id

    def from_json(self, json):
        self.id = json.get('tag_id', None)
        self.updated_on = json.get('updated_on', None)
        self.tag_name = json.get('tag_name', None)
        self.value = json.get('value', None)
        self.description = json.get('description', None)
        self.agent_id = json.get('agent_id', None)
        return self

    def to_dictionary(self):
        obj = {
            'tag_id': self.id,
            'updated_on': self.updated_on,
            'tag_name': self.tag_name,
            'value': self.value,
            'description': self.description,
            'agent_id': self.agent_id
        }
        return obj
