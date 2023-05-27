from django.db import models
from modules.models import Module
from teachers.models import Teacher
# Create your models here.

class Sunday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'

class Monday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'
    
class Tuesday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'
    
class Wednesday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'

class Thursday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'

class Friday(models.Model):
    Teacher_ID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Module_ID = models.ForeignKey(Module, on_delete=models.CASCADE)
    Time = models.TimeField()
    def __str__(self):
        return self.Module_ID + ' (' + self.Time + ')'
