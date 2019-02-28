#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)


SKILLS = {}


class Skill:
    name: str
    endpoint: str

    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint

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
