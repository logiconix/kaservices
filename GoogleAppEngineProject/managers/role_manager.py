from google.appengine.ext import ndb
from utility.permissions import TOKEN_TEST_API, TOKEN_READ_PROVIDERS, ROLE_APP_CLIENT, ROLE_BASIC_USER, \
    TOKEN_READ_GROUPS, TOKEN_WRITE_FORUM, TOKEN_READ_FORUM

__author__ = 'Michael'

class RoleModel(ndb.Model):
    roleName = ndb.StringProperty()
    permissions = ndb.StringProperty(repeated=True)

def get_permissions(role):
    role_model = RoleModel.query().filter(RoleModel.roleName == role).get()
    return role_model.permissions

def bootstrap():
    role = RoleModel()
    role.roleName = ROLE_APP_CLIENT
    role.permissions = [TOKEN_TEST_API, TOKEN_READ_PROVIDERS]
    role.put()

    role = RoleModel()
    role.roleName = ROLE_BASIC_USER
    role.permissions = [TOKEN_TEST_API, TOKEN_READ_GROUPS, TOKEN_READ_FORUM, TOKEN_WRITE_FORUM]
    role.put()
