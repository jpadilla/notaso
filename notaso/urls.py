from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notaso.views.home', name='home'),
    url(r'^universities/', include('universities.urls')),
    url(r'^register/', include('users.urls', namespace = 'users')),
    url(r'^professor/', include('professors.urls', namespace='professors')),

    url(r'^admin/', include(admin.site.urls)),
)
