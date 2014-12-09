import logging
from webob.exc import HTTPUnauthorized
from managers.authorization_manager import initialize_client
from utility.permissions import CLIENT_REGISTRY_KEY

__author__ = 'Michael'

AUTH_HEADER_KEY = 'Authorization'
PROVIDER_URL_KEY = 'provider_id'


def authorize(request):
    logging.info("Authorizing REQUEST: " + str(request.__dict__))

    auth_header = request.headers.get(AUTH_HEADER_KEY)
    if auth_header is None:
        logging.warning('Request contained no authorization header')
        raise HTTPUnauthorized()

    logging.info("AUTH_HEADER: " + auth_header)

    auth_provider = request.route_kwargs.get(PROVIDER_URL_KEY)
    if auth_provider:
        logging.info ("AUTH_PROVIDER: " + auth_provider)

    client = initialize_client(auth_header, auth_provider)
    request.registry[CLIENT_REGISTRY_KEY] = client
    return
