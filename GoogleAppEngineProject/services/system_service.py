import json
from managers import provider_manager
from model.provider import ProviderEncoder
from utility.secure_handler import SecureHandler
from utility.permissions import TOKEN_READ_PROVIDERS

__author__ = 'Michael'

class ProviderHandler(SecureHandler):
    def get(self):
        self.check_permission(TOKEN_READ_PROVIDERS)

        providers = provider_manager.get_all_providers()

        self.response.content_type = 'application/json'
        self.response.write(json.dumps(providers, cls=ProviderEncoder))
