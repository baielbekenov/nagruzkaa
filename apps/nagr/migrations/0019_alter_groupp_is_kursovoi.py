# Generated by Django 4.0.3 on 2022-10-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0018_discipline_is_kursovoi_groupp_is_kursovoi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='is_kursovoi',
            field=models.BooleanField(default=False, verbose_name='Курсовой'),
        ),
    ]