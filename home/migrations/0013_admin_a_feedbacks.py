# Generated by Django 5.0.4 on 2024-05-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_student_s_attdcd_student_s_attdcn_student_s_attddbms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='a_feedbacks',
            field=models.TextField(blank=True, default=''),
        ),
    ]