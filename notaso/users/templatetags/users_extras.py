import urllib
import hashlib

from django import template
register = template.Library()


@register.filter(name='gravatar_url')
def gravatar_url(instance, email):
    size = 40
    gravatar_url = "http://www.gravatar.com/avatar/"+ hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d': "retro", 's': str(size)})
    return gravatar_url
