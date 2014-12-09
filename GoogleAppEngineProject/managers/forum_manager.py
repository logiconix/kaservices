import logging
from google.appengine.ext import ndb
import time
from model.message import MessageModel

__author__ = 'Michael Landes'


def search_feed(group_kid, type=None, parent=None):
    group_key = ndb.Key(urlsafe=group_kid) if group_kid else None
    query = MessageModel.query(ancestor=group_key)

    if type:
        query = query.filter(MessageModel.type == type)
    if parent:
        query = query.filter(MessageModel.parent_message == parent)

    message_models = query.order(-MessageModel.date_hidden).fetch()
    return message_models


def kudo_messages(message_list, user):
    results = []
    userkey = user.key.urlsafe()

    for message_key in message_list:
        mkey = ndb.Key(urlsafe=message_key)
        message = mkey.get()
        if userkey not in message.kudos:
            message.kudos.append(userkey)
        message.put()

        results.append(message)

    return results

def insert_message(group_kid, message):
    group_key = ndb.Key(urlsafe=group_kid) if group_kid else None

    message_model = MessageModel(parent=group_key)
    message_model.text = message.text
    message_model.type = message.type
    message_model.parent_message = message.parent_message
    message_model.user_id = message.user_id
    message_model.username = message.username
    key = message_model.put()

    message_model = key.get()

    return message_model


def bootstrap(group_key, user0, user1, user2, user3):
    message = MessageModel(parent=group_key)
    message.text = "Welcome to class!"
    message.type = 'comment'
    message.put()
    time.sleep(1)

    message = MessageModel(parent=group_key)
    message.text = "I am so excited for this class!!!"
    message.type = 'comment'
    message.user_id = user0.urlsafe()
    message.username = user0.get().username
    message.put()
    time.sleep(1)

    message = MessageModel(parent=group_key)
    message.text = "Do we really need the book?"
    message.type = 'question'
    message.user_id = user0.urlsafe()
    message.username = user0.get().username
    parent_key = message.put()
    time.sleep(1)

    message = MessageModel(parent=group_key)
    message.text = "My roommate said we didn't need it"
    message.type = 'response'
    message.parent_message = parent_key.urlsafe()
    message.user_id = user1.urlsafe()
    message.username = user1.get().username
    message.put()
    time.sleep(1)

    message = MessageModel(parent=group_key)
    message.text = "This teacher is hilarious"
    message.type = 'comment'
    message.user_id = user2.urlsafe()
    message.username = user2.get().username
    message.put()
    time.sleep(1)

    message = MessageModel(parent=group_key)
    message.text = "I already got it and it is super helpful"
    message.type = 'response'
    message.user_id = user3.urlsafe()
    message.parent_message = parent_key.urlsafe()
    message.username = user3.get().username
    message.put()
    time.sleep(1)
