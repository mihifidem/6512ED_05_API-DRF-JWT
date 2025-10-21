from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, CategoryViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls
