from django.db import models

# Create your models here.


class Course(models.Model):
    course_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name + " (" + self.course_id + ")"
