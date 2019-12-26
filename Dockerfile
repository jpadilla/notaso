FROM python:3.7-alpine3.8

ENV LANG en_US.utf8

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps build-base

RUN apk add --no-cache \
  git \
  postgresql-dev \
  libffi-dev

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
