import urllib
import hashlib

from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='gravatar_url')
def gravatar_url(instance, email):
    size = 40
    hash = hashlib.md5(email.lower()).hexdigest()
    params = urllib.urlencode({'d': "retro", 's': str(size)})

    return "{}://www.gravatar.com/avatar/{}?".format(
        settings.PROTOCOL, hash, params)


@register.filter(name='avatar_https')
def avatar_https(instance, url):
    url = url.replace("http", "https", 1)
    return url.replace("httpss", "https", 1)
