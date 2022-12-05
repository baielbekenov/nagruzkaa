# Generated by Django 4.0.3 on 2022-12-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0035_alter_coppect_stavka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coppect',
            name='shtatnye_budget',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Штатные единицы/Бюджет'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='shtatnye_contract_ochnoe',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Штатные единицы/контракт/очное'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='shtatnye_contract_zaochnoe',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Штатные единицы/контракт/заочное'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='stavka',
            field=models.FloatField(blank=True, null=True, verbose_name='Ставка'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='ucheb_budget',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Учебная нагрузка/Бюджет'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='ucheb_contract_ochnoe',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Учебная нагрузка/контракт/очное'),
        ),
        migrations.AlterField(
            model_name='coppect',
            name='ucheb_contract_zaochnoe',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Учебная нагрузка/контракт/заочное'),
        ),
    ]
