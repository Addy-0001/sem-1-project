from django.db import models
from courses.models import Course
from modules.models import Module


class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return self.name + " (" + self.student_id + ")"
