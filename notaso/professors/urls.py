from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.create_professor_view, name='create_professor'),
    url(r'^(?P<professors_slug>[-_\w]+)/$', views.specific_professor_view,
        name='specified_professor'),
)
