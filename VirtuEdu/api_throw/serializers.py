from rest_framework import serializers
from users.models import Profile
from courses.models import Course, Module, Routine
from attendance.models import Attendance
from blog.models import Blog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email', 'password')


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
