# Generated by Django 4.0.3 on 2022-10-17 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0002_alter_groupp_for_discipline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupp',
            name='for_discipline',
        ),
    ]
