import json
import logging
from google.appengine.ext import ndb

__author__ = 'Michael Landes'


class DataModel(ndb.Model):
    def __init__(self, *args, **kwds):
        self._excluded = None
        super(DataModel, self).__init__(*args, **kwds)
        for key in self.to_dict().keys():
            if key.endswith('_hidden'):
                self.exclude(key)

    def exclude(self, key):
        if not self._excluded:
            self._excluded = []
        self._excluded.append(key)

    def get_dict(self):
        model_dict = self.to_dict(exclude=self._excluded)
        model_dict["id"] = self.key.urlsafe()
        return model_dict
    pass


class DataModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, DataModel):
            return super(DataModelEncoder, self).default(obj)

        return obj.get_dict()
    pass
