from django.urls import path

from . import views

app_name = "professors"

urlpatterns = [
    path("create/", views.CreateProfessorView.as_view(), name="create_professor"),
    path(
        "<slug:professors_slug>/",
        views.ProfessorView.as_view(),
        name="specified_professor",
    ),
]
