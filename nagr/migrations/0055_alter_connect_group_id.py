# Generated by Django 4.0.3 on 2022-12-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0054_groupp_rukovodstvo_dekanatom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='group_id',
            field=models.ManyToManyField(to='nagr.groupp', verbose_name='Группа'),
        ),
    ]
