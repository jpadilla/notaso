from django.urls import include, path

from . import views

app_name = "universities"

urlpatterns = [
    path("", views.UniversitiesView.as_view(), name="universities"),
    path("<slug:slug>/", views.UniversityView.as_view(), name="specified_university"),
    path("<slug:slug>/", include("notaso.departments.urls")),
]
