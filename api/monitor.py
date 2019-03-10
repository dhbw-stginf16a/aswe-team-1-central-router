#!/usr/bin/env python3

import logging
import requests

from api.models.MonitoringEntity import MonitoringEntity, MONENT_MANAGER
from api.models.Skill import Skill, SKILLS

logger = logging.getLogger(__name__)

def registerMonitor(body):
    MONENT_MANAGER.register(MonitoringEntity(body["concern"], body["endpoint"]))
    return "", 204

def getMonitor():
    return MONENT_MANAGER.getConcerns()

def dynamicPull(body, concern):
    return MONENT_MANAGER.requestConcern(concern, body["type"], body["payload"])

def handleEvent(body, concern):
    for skill in SKILLS:
        skill.pushEventIfInterested(concern, body["type"], body["payload"])
    return "", 204
