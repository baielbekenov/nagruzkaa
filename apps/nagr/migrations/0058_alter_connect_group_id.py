# Generated by Django 4.0.3 on 2022-12-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0057_alter_connect_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='group_id',
            field=models.ManyToManyField(to='nagr.group', verbose_name='Группа'),
        ),
    ]