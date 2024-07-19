# Generated by Django 5.0.4 on 2024-05-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_student_s_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stuDetails',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_marks',
            new_name='s_marksCD',
        ),
        migrations.AddField(
            model_name='student',
            name='s_marksCN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='s_marksDBMS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='s_marksOOPS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='s_marksOS',
            field=models.IntegerField(default=0),
        ),
    ]
