# Generated by Django 5.0.4 on 2024-05-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_faculty_f_password_student_s_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='f_alerts',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='student',
            name='s_alerts',
            field=models.CharField(default='', max_length=500),
        ),
    ]
