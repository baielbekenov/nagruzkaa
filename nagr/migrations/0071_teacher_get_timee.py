# Generated by Django 4.0.3 on 2022-12-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0070_groupp_sovmest_alter_teacher_is_budget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='get_timee',
            field=models.FloatField(default=0),
        ),
    ]