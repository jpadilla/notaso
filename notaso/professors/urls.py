from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(
        r'^create/$',
        views.CreateProfessorView.as_view(),
        name='create_professor'
    ),
    url(
        r'^(?P<professors_slug>[-\w]+)/$',
        views.ProfessorView.as_view(),
        name='specified_professor'
    ),
)
