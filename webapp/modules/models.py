from django.db import models
from courses.models import Course
# Create your models here.


class Module(models.Model):
    model_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " (" + self.model_id + ")"
