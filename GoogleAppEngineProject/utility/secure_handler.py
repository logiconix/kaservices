import logging
import webapp2
from utility.authorization_service import authorize, CLIENT_REGISTRY_KEY

__author__ = 'Michael'


class SecureHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        super(SecureHandler, self).__init__(request, response)

        authorize(request)

        client = self.request.registry.get(CLIENT_REGISTRY_KEY)
        self.access_tokens = client.permissions
        self.user = client.user
        return

    def check_permission(self, token):
        if token not in self.access_tokens:
            logging.warning("aborting, token not authorized: " + token)
            self.abort(401)
        return
