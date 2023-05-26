from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.IntegerField()
    number_of_exercises = models.IntegerField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name