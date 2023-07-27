from django.db import models
# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=10, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=1500)
    modules = models.ManyToManyField('Module', blank=False)

    def __str__(self):
        return self.course_name + " (" + self.course_id + ")"


class Module(models.Model):
    module_id = models.CharField(max_length=10, primary_key=True)
    module_name = models.CharField(max_length=100)
    module_description = models.CharField(max_length=1500)
    tutor_name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()

    def __str__(self):
        return self.module_name + " (" + self.module_id + ")"


class Routine(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.module.module_name + " (" + self.day + ")"
