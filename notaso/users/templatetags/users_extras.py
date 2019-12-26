import hashlib
import urllib.error
import urllib.parse
import urllib.request

from django import template

register = template.Library()


@register.filter(name="gravatar_url")
def gravatar_url(instance, email):
    size = 40
    hash = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
    params = urllib.parse.urlencode({"d": "retro", "s": str(size)})

    return f"https://www.gravatar.com/avatar/{hash}?{params}"


@register.filter(name="avatar_https")
def avatar_https(instance, url):
    url = url.replace("http", "https", 1)
    return url.replace("httpss", "https", 1)
