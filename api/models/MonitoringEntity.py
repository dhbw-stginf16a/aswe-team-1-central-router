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
        return json_resp, r.status_code

    def requestIfConcern(self, concern, rtype, payload):
        if self.concern == concern:
            print("Do Request")
            resps, status_code = self.request(rtype, payload)
            return resps, status_code
        else:
            print("Not matching")
            return [], 404

class MonitoringEntityManager:
    def __init__(self):
        self.monents = []

    def register(self, monent):
        self.monents.append(monent)

    def requestConcern(self, concern, rtype, payload):
        responses = []
        return_code = 200
        for monent in self.monents:
            resps, status_code = monent.requestIfConcern(concern, rtype, payload)
            if status_code >= 500:
                return_code = max(return_code, status_code)
            for resp in resps:
                responses.append(resp)

        return responses, return_code

    def getConcerns(self):
        return [monent.getConcern() for monent in self.monents]

MONENT_MANAGER = MonitoringEntityManager()
