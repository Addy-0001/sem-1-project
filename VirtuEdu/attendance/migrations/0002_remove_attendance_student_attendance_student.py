# Generated by Django 4.2.2 on 2023-06-24 15:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
