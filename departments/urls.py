from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<department_slug>[-_\w]+)/$', 'departments.views.department_view'),
)
