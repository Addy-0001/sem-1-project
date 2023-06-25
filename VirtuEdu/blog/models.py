from django.db import models
from users.models import Profile
from courses.models import Course, Module
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=100)
    HtmlContent = HTMLField(default='')
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    def __str__(self):
        return self.Title