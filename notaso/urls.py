from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="notaso api")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("notaso.users.urls", namespace="users")),
    path("", include("notaso.home.urls", namespace="home")),
    path(
        "universities/", include("notaso.universities.urls", namespace="universities")
    ),
    path("professors/", include("notaso.professors.urls", namespace="professors")),
    path("search/", include("notaso.search.urls", namespace="search")),
    # Static pages
    path(
        "legal/", TemplateView.as_view(template_name="static/legal.html"), name="legal"
    ),
    # Rest api
    path("api/", include("notaso.restapi.urls")),
    path("api/v2/", include("notaso.restapiv2.urls")),
    # Rest api Doc
    path("docs/", schema_view),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
