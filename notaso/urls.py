from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    # Prefix
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^', include('notaso.home.urls', namespace='home')),

    url(r'^universities/',
        include('notaso.universities.urls', namespace='universities')),

    url(r'^', include('notaso.users.urls', namespace='users')),

    url(r'^professors/',
        include('notaso.professors.urls', namespace='professors')),

    url(r'^search/', include('notaso.search.urls', namespace='search')),
)
