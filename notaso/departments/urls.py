from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<department_slug>[-_\w]+)/$',
    'departments.views.department_view', name="specified_department"),
)
