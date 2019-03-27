#!/usr/bin/env python3

import logging
import os

import requests

from api.models.Skill import Skill, SKILLS

logger = logging.getLogger(__name__)

CHAT_ADAPTER_URL = os.environ.setdefault('CHAT_ADAPTER_URL', 'localhost:8082/api/v1')


def registerSkill(body):
    SKILLS[body['name']] = Skill(body['name'], body['endpoint'], body['interests'])

    return '', 204

def getSkills():
    return list(SKILLS.keys()), 200

def proactive(body):
    try:
        requests.post(f'{CHAT_ADAPTER_URL}/proactive', json=body)
    except requests.ConnectionError:
        logger.error('Timeout on connection to chat adapter')
    finally:
        return '', 204
