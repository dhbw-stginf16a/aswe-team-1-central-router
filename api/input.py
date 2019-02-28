#!/usr/bin/env python3

import logging

from api.models.Skill import SKILLS

logger = logging.getLogger(__name__)


def intentInput(body):
    skill = SKILLS[body['skill']]

    # TODO: Do some handle<->user mapping here
    user = body['user_handle']
    response = skill.requestData(body['payload'], user)
    return response, 200
