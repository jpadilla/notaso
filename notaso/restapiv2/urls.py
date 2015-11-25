from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'universities', views.UniversityViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'departments', views.DepartmentViewSet)

urlpatterns = router.urls

urlpatterns += patterns('',
    url(r'^auth/$', include('rest_framework.urls',
                            namespace='rest_framework')),
)
