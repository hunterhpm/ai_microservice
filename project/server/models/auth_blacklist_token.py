import datetime

from project.server.managers.database import db


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime(), nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def from_partial_json(self, dictionary):
        super(BlacklistToken, self).from_partial_json(dictionary)
        self.token = dictionary['token']
        self.blacklisted_on = datetime.datetime.now()
        return self

    def from_json(self, json):
        self.token = json.get('token', None)
        self.blacklisted_on = json.get('blacklisted_on', None)
        return self

    def to_dictionary(self):
        return {
            'token': self.token,
            'blacklisted_on': self.blacklisted_on,
        }

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False