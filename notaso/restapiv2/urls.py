from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'universities', views.UniversityViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'departments', views.DepartmentViewSet)

urlpatterns = router.urls
