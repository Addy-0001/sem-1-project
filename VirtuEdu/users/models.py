from django.db import models
from django.contrib.auth.models import User
from courses.models import Course



class Profile(models.Model):
    # if user is deleted, delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'