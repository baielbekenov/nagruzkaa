# Generated by Django 4.0.3 on 2022-12-14 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0060_groupp_kontrol_itogovy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupp',
            name='kontrol_itogovy',
        ),
    ]