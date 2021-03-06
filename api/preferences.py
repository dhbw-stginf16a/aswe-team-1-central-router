#!/usr/bin/env python3

import logging
import os, atexit, shelve

logger = logging.getLogger(__name__)

class PreferenceStore:
    def __init__(self, path):
        self.store = shelve.open(path, "c")
        atexit.register(self.sync)

    def ensure_scope(self, scope):
        if str(scope) not in self.store:
            self.store[str(scope)] = dict()
            pass

    def update(self, scope, key, value):
        self.ensure_scope(scope)

        temp = self.store[str(scope)]
        if value is not None:
            temp[str(key)] = str(value)
        else:
            temp.pop(str(key), None) # Return None if it didn't exist to prevent an exception
        self.store[str(scope)] = temp

    def get(self, scope, key):
        self.ensure_scope(scope)
        return self.store[str(scope)][str(key)]

    def get_all(self, scope):
        self.ensure_scope(scope)
        return self.store[str(scope)].copy()

    def sync(self):
        logger.info("Syncing PreferenceStore to disk...")
        self.store.sync()

    def reset_scope(self, scope):
        self.ensure_scope(scope)
        self.store[str(scope)] = dict()

class ScopedPreferenceStore:
    def __init__(self, store, scope):
        self.store = store
        self.scope = scope

    def update(self, key, value):
        return self.store.update(self.scope, key, value)

    def get(self, key):
        return self.store.get(self.scope, key)

    def get_all(self):
        return self.store.get_all(self.scope)

    def sync(self):
        self.store.sync()

    def reset(self):
        self.store.reset_scope(self.scope)


preferenceStore = PreferenceStore(os.environ["PREFSTORE_LOCATION"])
globalPreferenceStore = ScopedPreferenceStore(preferenceStore, "global")

# Return a scoped preference store for the specific user id
def userPreferenceStore(user_id):
    return ScopedPreferenceStore(preferenceStore, "user-" + str(user_id))


def getUserPreferences(userId):
    return userPreferenceStore("test").get_all()

def patchUserPreferences(userId, body):
    prefStore = userPreferenceStore("test")
    for key in body:
        prefStore.update(key, body[key])
    return "", 204

def resetUserPreferences(userId):
    userPreferenceStore("test").reset()
    return "", 204

def getGlobalPreferences():
    return globalPreferenceStore.get_all()

def patchGlobalPreferences(body):
    for key in body:
        globalPreferenceStore.update(key, body[key])
    return "", 204
