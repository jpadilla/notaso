from django.conf.urls import url

from .views import DepartmentView

urlpatterns = [
    url(
        r"^(?P<department_slug>[-_\w]+)/$",
        DepartmentView.as_view(),
        name="specified_department",
    )
]
