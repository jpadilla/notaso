from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'universities.views.universities_view', name = 'universities'),
	url(r'^(?P<university_id>\d+)/$', 'universities.views.specific_university_view', name = 'specified_university'),
	url(r'^(?P<university_id>\d+)/', include('departments.urls'), name = 'departments'),	
)