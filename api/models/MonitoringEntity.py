#!/usr/bin/env python3

import logging
import requests

logger = logging.getLogger(__name__)


class MonitoringEntity:
    def __init__(self, concern, endpoint):
        self.concern = concern
        self.endpoint = endpoint.rstrip("/")

    def getConcern(self):
        return self.concern

    def getEndpoint(self):
        return self.endpoint

    def request(self, rtype, payload):
        r = requests.post("{}{}".format(self.endpoint, "/request"), json = { "type": rtype, "payload": payload })
        # assert r.status_code == 200
        json_resp = r.json()
        assert type(json_resp) == list
        return json_resp

    def requestIfConcern(self, concern, rtype, payload):
        if self.concern == concern:
            print("Do Request")
            return self.request(rtype, payload)
        else:
            print("Not matching")
            return []

class MonitoringEntityManager:
    def __init__(self):
        self.monents = []

    def register(self, monent):
        self.monents.append(monent)

    def requestConcern(self, concern, rtype, payload):
        responses = []

        for monent in self.monents:
            resps = monent.requestIfConcern(concern, rtype, payload)
            for resp in resps:
                responses.append(resp)

        return responses

    def getConcerns(self):
        return [monent.getConcern() for monent in self.monents]

MONENT_MANAGER = MonitoringEntityManager()
