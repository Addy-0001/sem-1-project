from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views


##########################this is the project level urls.py file####################

urlpatterns = [
    path('admin/', admin.site.urls), #this is the path to the admin site
    path('', views.home, name='home'),
    path("user/", include('users.urls')), #this is the path to the users app level urls.py file
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]