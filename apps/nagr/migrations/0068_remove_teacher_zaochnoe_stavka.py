# Generated by Django 4.0.3 on 2022-12-17 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0067_groupp_za_vsego_uchebnyh_chasov_groupp_zaochnoe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='zaochnoe_stavka',
        ),
    ]