# Generated by Django 4.0.3 on 2022-12-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0040_alter_teacher_job_title_alter_teacher_zvanie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=250, verbose_name='ФИО преподователя:'),
        ),
    ]
