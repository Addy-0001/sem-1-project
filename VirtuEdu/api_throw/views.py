from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer, CourseSerializer, ModuleSerializer, RoutineSerializer, AttendanceSerializer, BlogSerializer, BookSerializer, ContactSerializer
from users.models import User, Book
from courses.models import Course, Module, Routine
from attendance.models import Attendance
from blog.models import Blog


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = ContactSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
