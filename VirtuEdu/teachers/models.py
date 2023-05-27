from django.db import models
from modules.models import Module
from django.contrib.auth.models import User

class Teacher(models.Model):
    Teacher_ID = models.CharField(max_length = 20, primary_key=True)
    Name = User.username
    Email = models.EmailField(max_length=100)
    Password = User.password
    Module_ID = models.ManyToManyField(Module)
    User.is_staff = True
    def __str__(self):
        return self.Teacher_ID + ' (' + self.Name + ')'