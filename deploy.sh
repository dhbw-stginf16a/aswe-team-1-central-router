#!/bin/bash

tar -cf deploy.tar Pipfile Pipfile.lock openapi app.py api
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t asweteam1/central-router:latest -t asweteam1/central-router:$TRAVIS_TAG --label version="$TRAVIS_TAG" .
docker push asweteam1/central-router:latest
docker push asweteam1/central-router:$TRAVIS_TAG
