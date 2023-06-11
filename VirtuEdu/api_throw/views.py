from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, CourseSerializer, ModuleSerializer
from users.models import User
from courses.models import Course
from modules.models import Module


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class ModuleViewSet(viewsets.ModelViewSet):
   queryset = Module.objects.all()
   serializer_class = ModuleSerializer

