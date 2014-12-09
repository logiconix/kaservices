from google.appengine.ext import ndb
from utility.data_helper import DataModel

__author__ = 'Michael'


class UserModel(DataModel):
    username = ndb.StringProperty()
    role = ndb.StringProperty()
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty()
    authToken = ndb.StringProperty()
    coursesEnrolled = ndb.KeyProperty(repeated=True)
    #pinnedMessages = ndb.KeyProperty(repeated=True) TODO this is the ideal representation
    pinnedMessages = ndb.StringProperty(repeated=True)
