from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from rest_framework import routers

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'universities', views.UniversityViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'department', views.DepartmentViewSet)
router.register(r'search', views.SearchViewSet, base_name="search"),

urlpatterns = router.urls

#rest api urls
urlpatterns += patterns(
    '',
    url(r'^$', 'api_root'),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
