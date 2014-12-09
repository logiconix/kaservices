import json
from managers import group_manager
from model.group import GroupEncoder
from utility.authorization_service import PROVIDER_URL_KEY
from utility.permissions import TOKEN_READ_GROUPS
from utility.secure_handler import SecureHandler

__author__ = 'Michael Landes'

class HomeHandler(SecureHandler):
    def has_current_class(self):
        # determine if user's current schedule has a current class
        return False

    def get(self, *args, **kwargs):
        # redirect to the user's current class in the schedule
        # or send the user to the group selection page
        if self.has_current_class():
            # TODO (michael) redirect to user's current class in the schedule
            pass
        else:
            # redirect user to group selection page
            home_url = self.request.url
            group_url = home_url.replace("/home", "/groups") # TODO (michael) fix deprecated string function
            self.response.content_type = 'text/plain'
            self.response.body = group_url

class GroupHandler(SecureHandler):
    def get(self, *args, **kwargs):
        self.check_permission(TOKEN_READ_GROUPS)

        provider_id = self.request.route_kwargs.get(PROVIDER_URL_KEY)
        list = group_manager.get_all_groups(provider_id)

        self.response.content_type = 'application/json'
        self.response.body = json.dumps(list, cls=GroupEncoder)
