from django.urls import include, path
from rest_framework import routers
from api_throw.views import UserViewSet, BookViewSet, CourseViewSet, ModuleViewSet, RoutineViewSet, AttendanceViewSet, BlogViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'routine', RoutineViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'blog', BlogViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
