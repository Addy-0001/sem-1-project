from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, CourseSerializer, ModuleSerializer, AttendanceSerializer
from users.models import User
from courses.models import Course, Module
from attendance.models import Attendance


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
   queryset = Module.objects.all()
   serializer_class = ModuleSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
   queryset = Attendance.objects.all()
   serializer_class = AttendanceSerializer