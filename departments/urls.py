from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<department_id>\d+)/$', 'departments.views.department_view'),
)