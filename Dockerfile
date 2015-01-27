FROM google/python
MAINTAINER José Padilla <hello@jpadilla.com>

ENV PORT 8000

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get install -y \
        libxml2-dev \
        libxslt-dev \
        libpq-dev

WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["start"]
