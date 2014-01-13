from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<professor_id>\d+)/$', 'professors.views.specific_professor_view', name = 'specified_professor'),
)