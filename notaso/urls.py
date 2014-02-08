from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    # Prefix
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^universities/', include('universities.urls', namespace='universities')),
    url(r'^', include('users.urls', namespace='users')),
    url(r'^professors/', include('professors.urls', namespace='professors')),
)
