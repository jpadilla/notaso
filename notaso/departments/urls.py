from django.conf.urls import patterns, url

from .views import DepartmentView

urlpatterns = patterns(
    '',

    url(r'^(?P<department_slug>[-_\w]+)/$',
        DepartmentView.as_view(), name="specified_department"),
)
