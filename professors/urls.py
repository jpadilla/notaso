from django.conf.urls import patterns, include, url

from .views import ProfessorListView

urlpatterns = patterns(
    '',
    url(r'^$', ProfessorListView.as_view(), name='index'),
    url(r'^create/$', 'professors.views.create_professor_view', name='create_professor'),
    url(r'^(?P<professors_slug>[-_\w]+)/$', 'professors.views.specific_professor_view', name='specified_professor'),
)
