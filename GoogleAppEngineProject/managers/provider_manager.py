import logging
from google.appengine.ext import ndb
from model.provider import Provider

__author__ = 'Michael'

class ProviderModel(ndb.Model):
    providerName = ndb.StringProperty()
    officialName = ndb.StringProperty()

def get_provider_by_id(provider_id):
    if not provider_id:
        return None

    provider_model = ndb.Key(urlsafe=provider_id).get()

    if not provider_model:
        logging.info("Invalid Identifier: " + provider_id)
        return None

    provider = Provider()
    provider.id = provider_model.key.id()
    provider.providerName = provider_model.providerName
    provider.officialName = provider_model.officialName
    return provider


def get_all_providers():
    providers = ProviderModel.query().fetch()
    list = []
    for providerModel in providers:
        provider = Provider()
        provider.id = providerModel.key.urlsafe()
        provider.providerName = providerModel.providerName
        provider.officialName = providerModel.officialName
        list.append(provider)

    return list

def bootstrap():
    provider = ProviderModel()
    provider.providerName = 'system'
    provider.officialName = 'KudosApp System'
    provider.put()

    provider = ProviderModel()
    provider.providerName = 'ktech'
    provider.officialName = 'Kudos Institute of Technology'
    return provider.put()
