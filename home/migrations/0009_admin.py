# Generated by Django 5.0.4 on 2024-05-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_faculty_f_subcd_faculty_f_subcn_faculty_f_subdbms_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=50)),
                ('a_id', models.IntegerField()),
                ('a_password', models.CharField(default='', max_length=50)),
                ('a_alerts', models.TextField(default='')),
            ],
        ),
    ]