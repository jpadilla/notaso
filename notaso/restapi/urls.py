from rest_framework import routers

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"universities", views.UniversityViewSet)
router.register(r"professors", views.ProfessorViewSet)
router.register(r"department", views.DepartmentViewSet)
router.register(r"search", views.SearchViewSet, basename="search"),

urlpatterns = router.urls
