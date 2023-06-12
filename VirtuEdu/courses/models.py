from django.db import models
# Create your models here.


class Course(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=500)

    def __str__(self):
        return self.course_name + "(" + self.course_id + ")"
