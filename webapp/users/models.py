from django.db import models
from django.forms import ModelForm, PasswordInput


class studentUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username
