from django.db import models
from courses.models import Course

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    courses_teaching = models.ManyToManyField('courses.Course')
