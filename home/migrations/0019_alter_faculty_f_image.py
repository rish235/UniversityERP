# Generated by Django 5.0.4 on 2024-05-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_faculty_f_alerts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='f_image',
            field=models.ImageField(blank=True, upload_to='home/f_img'),
        ),
    ]
