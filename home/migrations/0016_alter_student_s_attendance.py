# Generated by Django 5.0.4 on 2024-05-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_student_s_marksswe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_attendance',
            field=models.FloatField(),
        ),
    ]
