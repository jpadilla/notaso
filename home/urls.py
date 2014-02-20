from django.conf.urls import patterns, include, url

from .views import home

urlpatterns = patterns(
    '',
    url(r'^$', home.as_view()),
)
