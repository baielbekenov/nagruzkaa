# Generated by Django 4.0.3 on 2022-12-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0043_alter_teacher_job_title_alter_teacher_ped_staj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='zaochnoe_stavka',
            field=models.FloatField(blank=True, null=True, verbose_name='Заочное ставка'),
        ),
    ]
