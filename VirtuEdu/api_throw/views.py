from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, CourseSerializer, ModuleSerializer, AttendanceSerializer, BlogSerializer
from users.models import User
from courses.models import Course, Module
from attendance.models import Attendance
from blog.models import Blog


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = ProfileSerializer


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
   queryset = Module.objects.all()
   serializer_class = ModuleSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
   queryset = Attendance.objects.all()
   serializer_class = AttendanceSerializer

class BlogViewSet(viewsets.ModelViewSet):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer