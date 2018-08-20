from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r"^$", views.UniversitiesView.as_view(), name="universities"),
    url(
        r"^(?P<slug>[-_\w]+)/$",
        views.UniversityView.as_view(),
        name="specified_university",
    ),
    url(r"^(?P<slug>[-_\w]+)/", include("notaso.departments.urls")),
]
