# Generated by Django 4.0.3 on 2022-12-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0062_groupp_kontrol_itogovyii'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='kontrol_itogovyii',
            field=models.FloatField(blank=True, null=True, verbose_name='Контроль/итоговый (экзамен)'),
        ),
    ]
