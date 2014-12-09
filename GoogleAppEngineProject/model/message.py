from google.appengine.ext import ndb
from utility.data_helper import DataModel

__author__ = 'Michael Landes'


class MessageModel(DataModel):
    text = ndb.StringProperty()
    type = ndb.StringProperty()
    parent_message = ndb.StringProperty()
    user_id = ndb.StringProperty()
    username = ndb.StringProperty()
    date_hidden = ndb.DateTimeProperty(auto_now_add=True)
    date = ndb.ComputedProperty(lambda self: str(self.date_hidden) if self.date_hidden else None)
    kudos = ndb.StringProperty(repeated=True)
