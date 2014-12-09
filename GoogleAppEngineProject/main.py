#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from services.forum_service import ForumHandler, KudoHandler
from services.group_service import HomeHandler, GroupHandler
from services.system_service import ProviderHandler
from services.test_service import Bootstrapper
from services.user_service import CurrentUserHandler, UserInformationHandler, UserMessagePinHandler

app = webapp2.WSGIApplication([
    webapp2.Route(r'/api/boot', handler=Bootstrapper, methods=['POST']), # TODO remove route once db up
    webapp2.Route(r'/api/system/providers', handler=ProviderHandler, methods=['GET']),
    webapp2.Route(r'/api/<provider_id>/users/current', handler=CurrentUserHandler, methods=['GET']),
    webapp2.Route(r'/api/<provider_id>/users/list', handler=UserInformationHandler, methods=['GET']),
    webapp2.Route(r'/api/<provider_id>/users/pin', handler=UserMessagePinHandler, methods=['POST']),
    webapp2.Route(r'/api/<provider_id>/home', handler=HomeHandler, methods=['GET']), # TODO method not necessary
    webapp2.Route(r'/api/<provider_id>/groups', handler=GroupHandler, methods=['GET']),
    webapp2.Route(r'/api/<provider_id>/groups/<group_id>/forum/messages', handler=ForumHandler, methods=['GET', 'POST']),
    webapp2.Route(r'/api/<provider_id>/groups/<group_id>/forum/messages/kudo', handler=KudoHandler, methods=['POST'])
], debug=True)
