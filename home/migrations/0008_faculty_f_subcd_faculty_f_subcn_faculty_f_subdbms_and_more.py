# Generated by Django 5.0.4 on 2024-05-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_studetails_rename_s_marks_student_s_markscd_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='f_subCD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faculty',
            name='f_subCN',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faculty',
            name='f_subDBMS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faculty',
            name='f_subOOPS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faculty',
            name='f_subOS',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='faculty',
            name='f_subSWE',
            field=models.BooleanField(default=False),
        ),
    ]