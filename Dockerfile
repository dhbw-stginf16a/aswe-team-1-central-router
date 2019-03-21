FROM python:3.6-alpine

LABEL maintainer="Thore Kruess"

RUN adduser -D flask && pip install pipenv && pip install gevent

WORKDIR /app

ADD deploy.tar /app/

RUN pipenv install --deploy --system && chown -R flask:flask /app

USER flask

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "-k", "gevent", "--worker-connections", "1000", "app:application"]
