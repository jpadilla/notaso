FROM python:2.7-slim
MAINTAINER José Padilla <hello@jpadilla.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
        libxml2-dev \
        libxslt-dev \
        libpq-dev \
        build-essential

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

# ENTRYPOINT ["./docker-entrypoint.sh"]

# CMD ["start"]
