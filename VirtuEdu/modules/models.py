from django.db import models
from courses.models import Course

class Module(models.Model):
    Module_ID = models.CharField(max_length = 20, primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.Module_ID + ' (' + self.Name + ')'