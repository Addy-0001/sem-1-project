from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.surname
        