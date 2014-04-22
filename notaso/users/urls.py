from django.conf.urls import patterns, url

from .views import SettingsView

urlpatterns = patterns(
    '',
    url(r'^settings/$', SettingsView.as_view(), name='settings'),
)
