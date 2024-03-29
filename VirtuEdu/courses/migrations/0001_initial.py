# Generated by Django 4.2.2 on 2023-06-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=100)),
                ('module_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.CharField(max_length=500)),
                ('modules', models.ManyToManyField(to='courses.module')),
            ],
        ),
    ]
