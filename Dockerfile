FROM python:2.7-alpine3.7

ENV LANG en_US.utf8

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps build-base

RUN apk add --no-cache \
  postgresql-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev

WORKDIR /app/

# Install application requirements
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app/
