# Generated by Django 5.0.4 on 2024-05-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_student_s_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_attendance',
            field=models.FloatField(default=0),
        ),
    ]