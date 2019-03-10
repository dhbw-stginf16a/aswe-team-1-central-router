#!/usr/bin/env python3

import logging
import requests

logger = logging.getLogger(__name__)


SKILLS = {}


class Skill:
    name: str
    endpoint: str

    def __init__(self, name, endpoint, interests):
        self.name = name
        self.endpoint = endpoint.rstrip("/")
        self.interests = interests

    def requestData(self, payload: dict, user: str) -> dict:
        """Allows to query the service with the data
        given by the intent detector

        Arguments:
            payload {dict} -- [description]
            user {str} -- [description]

        Returns:
            dict -- [description]
        """
        # Do some requests magic here and return the response
        logger.debug(self.endpoint)
        return {}

    def getInterests(self):
        return self.interests

    def pushEvent(self, concern, etype, payload):
        r = requests.post("{}{}{}".format(self.endpoint, "/event/", concern), json = {"type": etype, "payload": payload})
        assert r.status_code == 204

    def pushEventIfInterested(self, concern, etype, payload):
        if concern in self.getInterests():
            self.pushEvent(concern, etype, payload)
