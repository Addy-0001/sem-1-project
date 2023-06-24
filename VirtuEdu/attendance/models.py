from django.db import models
from courses.models import Module
from users.models import Profile
#Attendance model here 
class Attendance(models.Model):
    #attendance_id = models.CharField(max_length=10, primary_key=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    student = models.ManyToManyField(Profile)
    date = models.DateTimeField()
    present = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.module} - {self.date}'