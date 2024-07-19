# Generated by Django 5.0.4 on 2024-07-16 06:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]