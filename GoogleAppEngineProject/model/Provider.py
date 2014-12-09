import json

__author__ = 'Michael'

class Provider:
    def __init__(self):
        self.id = None
        self.providerName = None
        self.officialName = None

class ProviderEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, Provider):
            return super(ProviderEncoder, self).default(obj)

        return obj.__dict__