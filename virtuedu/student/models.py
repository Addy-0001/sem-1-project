from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 
    payment_status = models.BooleanField(default=False)
    readingCourses = models.ManyToManyField('courses.Course', related_name='readingCourses')

    def __str__(self):
        return self.name + " " + self.surname
        