from rest_framework import serializers
from users.models import Profile, Book, Contact
from courses.models import Course, Module, Routine
from attendance.models import Attendance
from blog.models import Blog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'user_course', 'books_issued')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'books_available', 'book_author',
                  'book_link', 'book_description')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('contact_name', 'email', 'message')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_id', 'course_name')


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('module_id', 'module_name')


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ('module', 'day', 'start_time', 'end_time')


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('module', 'student', 'date', 'present')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('Title', 'HtmlContent', 'Author', 'Module', 'Date')
