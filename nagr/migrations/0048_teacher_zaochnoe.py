# Generated by Django 4.0.3 on 2022-12-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0047_group_zaochnoe'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='zaochnoe',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
