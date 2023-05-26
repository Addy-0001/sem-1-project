from django.db import models
from courses.models import Course
from teachers.models import Teacher

class Module(models.Model):
    module_id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.module_id + ")"