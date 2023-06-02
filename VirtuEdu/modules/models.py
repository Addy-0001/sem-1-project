from django.db import models
from courses.models import Course
# Create your models here.


class Module(models.Model):
    module_id = models.CharField(max_length=10, primary_key=True)
    module_name = models.CharField(max_length=100)
    module_description = models.CharField(max_length=500)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.module_name + "(" + self.module_id + ")"
