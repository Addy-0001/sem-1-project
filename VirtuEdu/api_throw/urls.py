from django.urls import include, path
from rest_framework import routers
from api_throw.views import UserViewSet, CourseViewSet, ModuleViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)

urlpatterns = [
   path('', include(router.urls)),
]