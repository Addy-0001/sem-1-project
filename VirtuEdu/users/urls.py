from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
]

admin.site.site_header = "VirtuEdu Admin"
admin.site.site_title = "VirtuEdu Admin Portal"
