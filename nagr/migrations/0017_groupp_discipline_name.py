# Generated by Django 4.0.3 on 2022-10-26 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0016_alter_group_labrab_po_ucheb_planu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupp',
            name='discipline_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]