import hashlib
import logging
from google.appengine.ext import ndb
from model.user import UserModel
from utility.permissions import ROLE_APP_CLIENT, ROLE_BASIC_USER

__author__ = 'Michael'


def get_users_by_ids(user_ids):
    keys = []
    for user_id in user_ids:
        keys.append(ndb.Key(urlsafe=user_id))

    users = ndb.get_multi(keys)

    return users


def get_users_by_username(username, provider_key_id=None):
    ancestor_key = ndb.Key(urlsafe=provider_key_id) if provider_key_id else None

    users = UserModel.query(ancestor=ancestor_key).filter(UserModel.username == username)
    return users


def get_all_users(provider_key_id=None):
    ancestor_key = ndb.Key(urlsafe=provider_key_id) if provider_key_id else None

    users = UserModel.query(ancestor=ancestor_key).fetch()
    return users


def pin_messages(message_list, user):
    for mid in message_list:
        if mid not in user.pinnedMessages:
            logging.info('adding message: ' + mid)
            user.pinnedMessages.append(mid)

    user.put()

    return user


def bootstrap(provider_key):
    user_keys = []

    user = UserModel()
    user.username = 'webapp'
    user.role = ROLE_APP_CLIENT
    user.authToken = hashlib.md5('webapp').hexdigest()
    user.put()

    user = UserModel(parent=provider_key)
    user.username = 'mlandes3'
    user.firstName = 'Michael'
    user.lastName = 'Landes'
    user.authToken = hashlib.md5('mlandes3').hexdigest()
    user.role = ROLE_BASIC_USER
    user_keys.append(user.put())

    user = UserModel(parent=provider_key)
    user.username = 'pram8'
    user.firstName = 'Pranav'
    user.lastName = 'Ram'
    user.authToken = hashlib.md5('pram8').hexdigest()
    user.role = ROLE_BASIC_USER
    user_keys.append(user.put())

    user = UserModel(parent=provider_key)
    user.username = 'iwilson7'
    user.firstName = 'Ian'
    user.lastName = 'Wilson'
    user.authToken = hashlib.md5('iwilson7').hexdigest()
    user.role = ROLE_BASIC_USER
    user_keys.append(user.put())

    user = UserModel(parent=provider_key)
    user.username = 'yxi8'
    user.firstName = 'Yaohong'
    user.lastName = 'Xi'
    user.authToken = hashlib.md5('yxi8').hexdigest()
    user.role = ROLE_BASIC_USER
    user_keys.append(user.put())

    return user_keys
