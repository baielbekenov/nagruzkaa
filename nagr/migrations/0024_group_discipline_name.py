# Generated by Django 4.0.3 on 2022-10-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0023_remove_connect_discipline_id_alter_connect_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='discipline_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]