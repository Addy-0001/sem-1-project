# Generated by Django 4.2.2 on 2023-07-25 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_routine'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='credit_hours',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='tutor_name',
            field=models.CharField(default='Adamya', max_length=100),
            preserve_default=False,
        ),
    ]
