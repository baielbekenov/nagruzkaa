# Generated by Django 4.1.2 on 2022-11-06 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0028_remove_connect_academ_sov_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='is_budget',
            field=models.BooleanField(default=False, verbose_name='Бюджетный'),
        ),
    ]