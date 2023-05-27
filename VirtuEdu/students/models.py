from django.db import models
from courses.models import Course
from routines.models import Sunday, Monday, Tuesday, Wednesday, Thursday, Friday
from modules.models import Module
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    Student_ID = models.CharField(max_length = 20, primary_key=True)
    Name = User.username
    Email = models.EmailField(max_length=100)
    Password = User.password
    Course_ID = models.ForeignKey(Course, on_delete=models.CASCADE)
    Sunday_Routine = models.ManyToManyField(Sunday)
    Monday_Routine = models.ManyToManyField(Monday)
    Tuesday_Routine = models.ManyToManyField(Tuesday)
    Wednesday_Routine = models.ManyToManyField(Wednesday)
    Thursday_Routine = models.ManyToManyField(Thursday)
    Friday_Routine = models.ManyToManyField(Friday)
    User.is_staff = False
    def __str__(self):
        return self.Student_ID + ' (' + self.Name + ')'
