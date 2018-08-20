FROM python:2.7-alpine3.7

ENV LANG en_US.utf8

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps build-base

RUN apk add --no-cache \
  postgresql-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev

RUN pip install pipenv

WORKDIR /app/

COPY Pipfile Pipfile.lock /app/

# Install application requirements
RUN pip install pipenv && \
    pipenv install --deploy --system && \
    pip uninstall -y pipenv && \
    rm -rf /root/.cache

# Bundle app source
COPY . /app/
