from rest_framework import serializers
from users.models import User
from courses.models import Course
from modules.models import Module

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'course_description', 'course_image')
    
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'module_name', 'module_description', 'module_image')
