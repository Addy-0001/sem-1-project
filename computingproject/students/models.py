from django.db import models
from modules.models import Module
from courses.models import Course
# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    models = models.ManyToManyField(Module)

    def __str__(self):
        return self.name + " (" + self.student_id + ")"