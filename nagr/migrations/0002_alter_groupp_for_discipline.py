# Generated by Django 4.0.3 on 2022-10-17 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupp',
            name='for_discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline_group', to='nagr.discipline', verbose_name='Дисциплина'),
        ),
    ]