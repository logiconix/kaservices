import webapp2
from managers import group_manager, forum_manager, provider_manager, role_manager, user_manager

__author__ = 'Michael'


class Bootstrapper(webapp2.RequestHandler):
    def post(self):
        provider_key = provider_manager.bootstrap()
        role_manager.bootstrap()
        user0, user1, user2, user3 = tuple(user_manager.bootstrap(provider_key))
        group_key = group_manager.bootstrap(provider_key)
        forum_manager.bootstrap(group_key, user0, user1, user2, user3)
