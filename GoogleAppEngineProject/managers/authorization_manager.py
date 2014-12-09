import base64
import hashlib
import logging
from webob.exc import HTTPUnauthorized
from managers import role_manager, user_manager

__author__ = 'Michael'

class Client:
    def __init__(self, user):
        self.user = user
        self.permissions = role_manager.get_permissions(user.role)

def initialize_client(auth_header, auth_provider):
    scheme, parameters = auth_header.split(' ', 1)

    if scheme.upper() == 'BASIC':
        user = find_user_basic(parameters, auth_provider)
    else:
        user = None # TODO (michael) implement token based auth for provider

    if not user:
        logging.warning("could not match credentials to a user")
        raise HTTPUnauthorized()

    return Client(user)

def find_user_basic(parameters, auth_provider):
    """Find user according to BASIC credentials

    :param parameters: The parameter string from the HTTP Authentication header
    :param auth_provider: The provider or username-group of the user
    :return: User object, or None if user could not be found
    """

    value = base64.standard_b64decode(parameters)
    username, password = value.split(':', 1)

    # find the user by name (should be unique within provider group)
    users = user_manager.get_users_by_username(username, auth_provider).fetch()
    if len(users) != 1:
        logging.warning("username did not map to 1 user")
        return None

    # check that password is correct
    user = users[0]
    token = hashlib.md5(password).hexdigest()
    if user.authToken != token:
        logging.warning("incorrect password")
        return None

    return user
