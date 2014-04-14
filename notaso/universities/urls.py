from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns(
    # Prefix
    '',

    url(r'^$', views.universities_view, name='universities'),

    url(r'^(?P<slug>[-_\w]+)/$',
        views.specific_university_view, name='specified_university'),

    url(r'^(?P<slug>[-_\w]+)/',
        include('notaso.departments.urls')),
)
