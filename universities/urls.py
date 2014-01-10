from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'universities.views.universities_view'),
	url(r'^(?P<university_id>\d+)/$', 'universities.views.specific_university_view'),
	url(r'^(?P<university_id>\d+)/', include('departments.urls')),	
)