from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Profile(models.Model):
    # if user is deleted, delete profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)
    books_issued = models.ManyToManyField('Book', blank=True, default=None)

    def __str__(self):
        return f'{self.user.username} Profile'


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    books_available = models.IntegerField()
    book_author = models.CharField(max_length=100)
    book_link = models.CharField(max_length=100)
    book_description = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.contact_name
