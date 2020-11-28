from datetime import datetime
from flask.json import JSONEncoder

from project.server.helpers import date


class DefaultJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj is None:
                    return None
                return date.to_iso8601(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
