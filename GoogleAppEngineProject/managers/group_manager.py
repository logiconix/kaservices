from google.appengine.ext import ndb
from model.group import Group

__author__ = 'Michael Landes'


class GroupModel(ndb.Model):
    courseName = ndb.StringProperty()


def get_all_groups(provider_key_id):
    list = []

    if not provider_key_id:
        return list

    ancestor_key = ndb.Key(urlsafe=provider_key_id)
    group_models = GroupModel.query(ancestor=ancestor_key).fetch()

    for group_model in group_models:
        group = Group()
        group.id = group_model.key.urlsafe()
        group.courseName = group_model.courseName
        list.append(group)

    return list


def bootstrap(provider_key):
    group = GroupModel(parent=provider_key)
    group.courseName = 'CS 8803 - MAS'
    group_key = group.put()

    group = GroupModel(parent=provider_key)
    group.courseName = 'CS 101 - Intro to Programming'
    group.put()

    return group_key
