# Generated by Django 4.0.3 on 2022-12-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0030_remove_connect_itogo_remove_connect_itogo2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connect',
            name='shtatnye_budget',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='shtatnye_contract_ochnoe',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='shtatnye_contract_zaochnoe',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='shtatnye_vsego',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ucheb_budget',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ucheb_contract_ochnoe',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ucheb_contract_zaochnoe',
        ),
        migrations.RemoveField(
            model_name='connect',
            name='ucheb_vsego',
        ),
        migrations.AddField(
            model_name='connect',
            name='is_budget',
            field=models.BooleanField(default=False, verbose_name='Бюджетный'),
        ),
        migrations.AddField(
            model_name='connect',
            name='job_title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='connect',
            name='name',
            field=models.CharField(default=0, max_length=250, verbose_name='ФИО преподователя: '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connect',
            name='ped_staj',
            field=models.IntegerField(default=0, verbose_name='Пед стаж'),
        ),
        migrations.AddField(
            model_name='connect',
            name='shtat_edinicy_budget',
            field=models.FloatField(blank=True, null=True, verbose_name='Штатные единицы / бюджет'),
        ),
        migrations.AddField(
            model_name='connect',
            name='shtat_edinicy_kontrakt_zaochnoe',
            field=models.FloatField(blank=True, null=True, verbose_name='Штатные единицы / контракт / заочное'),
        ),
        migrations.AddField(
            model_name='connect',
            name='shtat_edinicy_vsego',
            field=models.FloatField(blank=True, null=True, verbose_name='Штатные единицы / всего'),
        ),
        migrations.AddField(
            model_name='connect',
            name='shtat_sovmest',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Штат.или совмест.'),
        ),
        migrations.AddField(
            model_name='connect',
            name='ucheb_nagruzka_Vsego',
            field=models.FloatField(blank=True, null=True, verbose_name='Учебная нагрузка / Всего'),
        ),
        migrations.AddField(
            model_name='connect',
            name='ucheb_nagruzka_budget',
            field=models.FloatField(blank=True, null=True, verbose_name='Учебная нагрузка / бюджет'),
        ),
        migrations.AddField(
            model_name='connect',
            name='ucheb_nagruzka_kontract_ochnoe',
            field=models.FloatField(blank=True, null=True, verbose_name='Учебная нагрузка / контракт / очное'),
        ),
        migrations.AddField(
            model_name='connect',
            name='ucheb_nagruzka_kontract_zaochnoe',
            field=models.FloatField(blank=True, null=True, verbose_name='Учебная нагрузка / контракт / заочное'),
        ),
        migrations.AddField(
            model_name='connect',
            name='zvanie',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Звание'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='ped_staj',
            field=models.IntegerField(default=0, verbose_name='Пед стаж'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='shtat_sovmest',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Штат.или совмест.'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='stavka_budget',
            field=models.FloatField(blank=True, null=True, verbose_name='Ставка бюджет'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='stavka_ochnoe',
            field=models.FloatField(blank=True, null=True, verbose_name='Ставка'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='zvanie',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Звание'),
        ),
    ]
