# Generated by Django 4.0.3 on 2022-12-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0045_alter_teacher_zaochnoe_stavka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='zaochnoe_stavka',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Заочная ставка'),
        ),
    ]
