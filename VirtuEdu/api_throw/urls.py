from django.urls import include, path
from rest_framework import routers
from api_throw.views import UserViewSet, BookViewSet, CourseViewSet, ModuleViewSet, RoutineViewSet, AttendanceViewSet, BlogViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'routine', RoutineViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
