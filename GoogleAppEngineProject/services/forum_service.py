import json
import logging
from managers import forum_manager
from model.message import MessageModel
from utility.data_helper import DataModelEncoder
from utility.permissions import TOKEN_READ_FORUM, TOKEN_WRITE_FORUM, CLIENT_REGISTRY_KEY
from utility.secure_handler import SecureHandler

__author__ = 'Michael Landes'


GROUP_URL_KEY = 'group_id'


class KudoHandler(SecureHandler):
    def post(self, *args, **kwargs):
        # TODO implement permissions
        client = self.request.registry.get(CLIENT_REGISTRY_KEY)

        message_list = self.request.POST.getall('mid')
        updated_messages = forum_manager.kudo_messages(message_list, client.user)

        self.response.content_type = 'application/json'
        self.response.body = json.dumps(updated_messages, cls=DataModelEncoder)
        return
    pass


class ForumHandler(SecureHandler):
    def __init__(self, request, response):
        super(ForumHandler, self).__init__(request, response)

        self.gid = self.request.route_kwargs.get(GROUP_URL_KEY)
        logging.info("GID is " + self.gid)

    def check_membership(self):
        client = self.request.registry.get(CLIENT_REGISTRY_KEY)
        user = None if not client else client.user
        if not user:
            return False

        # TODO (michael) actually check the user to see if they belong to the group
        logging.warning("Assuming membership in group for now...")
        return True

    def get(self, *args, **kwargs):
        self.check_permission(TOKEN_READ_FORUM)
        if not self.check_membership():
            self.abort(401)

        message_type = self.request.get('type', default_value=None)
        message_parent = self.request.get('parent', default_value=None)

        messages = forum_manager.search_feed(self.gid, message_type, message_parent)
        self.response.content_type = 'application/json'
        self.response.body = json.dumps(messages, cls=DataModelEncoder)

    def post(self, *args, **kwargs):
        self.check_permission(TOKEN_WRITE_FORUM)
        if not self.check_membership():
            self.abort(401)

        jobj = json.loads(self.request.body)
        message = MessageModel()
        message.text = jobj.get('text')
        message.type = jobj.get('type')
        message.parent_message = jobj.get('parent_message')
        message.user_id = self.user.key.urlsafe()
        message.username = self.user.username

        final_message = forum_manager.insert_message(self.gid, message)
        self.response.content_type = 'application/json'
        self.response.body = json.dumps(final_message, cls=DataModelEncoder)
