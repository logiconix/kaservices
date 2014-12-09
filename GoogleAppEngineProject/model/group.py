import json

__author__ = 'Michael Landes'

class Group:
    def __init__(self):
        self.id = None
        self.courseName = None

class GroupEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Group):
            return super(GroupEncoder, self).default(obj)

        return obj.__dict__