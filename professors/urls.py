from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<professor_id>\d+)/$', 'professors.views.specific_professor_view', name = 'specified_professor'),
    url(r'^create/$', 'professors.views.create_professor_view', name = 'create_professor'),
    url(r'^(?P<professor_id>\d+)/comment/$', 'professors.views.post_comment', name='comment'),
)