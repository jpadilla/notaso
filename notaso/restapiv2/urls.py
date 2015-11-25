from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter

from . import views

routerv2 = DefaultRouter()
routerv2.register(r'universities', views.UniversityViewSet)
routerv2.register(r'professors', views.ProfessorViewSet)
routerv2.register(r'departments', views.DepartmentViewSet)


urlpatterns = patterns('',
    url(r'^', include(routerv2.urls)),

    url(r'^auth/$', include('rest_framework.urls',
                            namespace='rest_framework')),
)
