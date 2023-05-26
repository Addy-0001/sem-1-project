from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + " - " + self.teacher_id