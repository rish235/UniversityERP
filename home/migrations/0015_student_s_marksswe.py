# Generated by Django 5.0.4 on 2024-05-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_student_s_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='s_marksSWE',
            field=models.IntegerField(default=0),
        ),
    ]
