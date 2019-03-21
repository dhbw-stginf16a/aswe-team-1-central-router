FROM python:3.6-alpine

LABEL maintainer="Thore Kruess"

RUN adduser -D flask && pip install pipenv
RUN apk add --update --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main py-gevent


WORKDIR /app

ADD deploy.tar /app/

RUN pipenv install --deploy --system && chown -R flask:flask /app

USER flask

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "-k", "gevent", "--worker-connections", "1000", "app:application"]
