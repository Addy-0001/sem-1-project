from django.db import models

# Create your models here.
class Course(models.Model):
    Course_ID = models.CharField(max_length = 20, primary_key=True)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)

    def __str__(self):
        return self.Course_ID + ' (' + self.Name + ')'

