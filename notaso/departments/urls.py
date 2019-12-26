from django.urls import path

from .views import DepartmentView

urlpatterns = [
    path(
        "<slug:department_slug>/", DepartmentView.as_view(), name="specified_department"
    )
]
