from django.conf.urls import patterns, url

from .views import department_view

urlpatterns = patterns(
    '',

    url(r'^(?P<department_slug>[-_\w]+)/$',
        department_view, name="specified_department"),
)
