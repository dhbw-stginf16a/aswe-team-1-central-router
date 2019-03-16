#!/usr/bin/env python3

import logging

from api.models.Skill import SKILLS

logger = logging.getLogger(__name__)


def intentInput(body):
    skill = SKILLS[body['skill']]

    response = skill.requestData(body['type'], body['payload'], body['user_handle'], body['input_service'])
    return response, 200
