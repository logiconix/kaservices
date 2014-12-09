import json
import logging
from managers import user_manager
from utility.authorization_service import PROVIDER_URL_KEY
from utility.data_helper import DataModelEncoder
from utility.permissions import CLIENT_REGISTRY_KEY
from utility.secure_handler import SecureHandler

__author__ = 'Michael Landes'


class CurrentUserHandler(SecureHandler):
    def get(self, *args, **kwargs):
        # no permissions needed, this method can be used for validation of access
        client = self.request.registry.get(CLIENT_REGISTRY_KEY)
        user = client.user

        user.exclude('authToken')
        user.exclude('role')

        self.response.content_type = 'application/json'
        self.response.body = json.dumps(user, cls=DataModelEncoder)
        return
    pass


class UserMessagePinHandler(SecureHandler):
    def post(self, *args, **kwargs):
        # TODO implement permissions, or none needed
        client = self.request.registry.get(CLIENT_REGISTRY_KEY)

        message_list = self.request.POST.getall('mid')
        updated_user = user_manager.pin_messages(message_list, client.user)

        updated_user.exclude('authToken')
        updated_user.exclude('role')

        self.response.content_type = 'application/json'
        self.response.body = json.dumps(updated_user, cls=DataModelEncoder)
        return
    pass


class UserInformationHandler(SecureHandler):
    def get(self, *args, **kwargs):
        # self.check_permission(TOKEN_GET_BASIC_USER_INFORMATION) TODO implement

        # user_id_list = self.request.POST.getall('id')
        auth_provider = self.request.route_kwargs.get(PROVIDER_URL_KEY)

        # user_list = user_manager.get_users_by_ids(user_id_list)
        user_list = user_manager.get_all_users(auth_provider)
        for user in user_list:
            user.exclude('authToken')
            user.exclude('role')
            user.exclude('coursesEnrolled')

        self.response.content_type = 'application/json'
        self.response.body = json.dumps(user_list, cls=DataModelEncoder)
        return
    pass
