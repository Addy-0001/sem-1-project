from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from api_throw.views import UserViewSet, CourseViewSet, ModuleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'modules', ModuleViewSet)


##########################this is the project level urls.py file####################

urlpatterns = [
    path('admin/', admin.site.urls), #this is the path to the admin site
    path('', views.home, name='home'),
    path("user/", include('users.urls')), #this is the path to the users app level urls.py file
    path("api_virtuedu/", include('api_throw.urls')), #this is the path to the courses app level urls.py file

]