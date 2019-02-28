#!/usr/bin/env python3

import logging

from api.models.Skill import Skill, SKILLS

logger = logging.getLogger(__name__)


def registerSkill(body):
    SKILLS[body['name']] = Skill(body['name'], body['endpoint'])

    return '', 204

def getSkills():
    return list(SKILLS.keys()), 200
