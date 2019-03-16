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

    def requestData(self, etype: str, payload: dict, user_handle: str, input_service: str) -> dict:
        """Allows to query the service with the data
        given by the intent detector

        Arguments:

        Returns:
            dict -- [description]
        """
        user = "{}#{}".format(user_handle, input_service)
        r = requests.post("{}{}".format(self.endpoint, "/request"), json = {
            "type": etype,
            "payload": payload,
            "user": user
        })
        assert r.status_code == 200
        json_r = r.json()
        assert type(json_r) == dict
        return json_r

    def getInterests(self):
        return self.interests

    def pushEvent(self, concern, etype, payload):
        r = requests.post("{}{}{}".format(self.endpoint, "/event/", concern), json = {"type": etype, "payload": payload})
        assert r.status_code == 204

    def pushEventIfInterested(self, concern, etype, payload):
        if concern in self.getInterests():
            self.pushEvent(concern, etype, payload)
