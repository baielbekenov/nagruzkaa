# Generated by Django 4.0.3 on 2022-10-25 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nagr', '0014_teacher_academ_sov_teacher_aspi_doctoron_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupp',
            name='academ_sov',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='aspirantura_doctorontura',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='kontrol_itogovyi',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='kontrol_tekuchiy1',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='kontrol_tekuchiy2',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='kontrol_tekuchiy3',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='magistratura',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='normokontr',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='offline',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='online',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='praktika_nauchno',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='praktika_pedagog',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='praktika_predkval',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='praktika_proizvod',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='praktika_uchebnay',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='priem_SRS',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='prochie',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='recenzirov_KR',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='rukovod_KRIKP',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='rukovodstvo_dekanatom',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='rukovodstvo_kafedroi',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='vsego_uchebnyh_chasov',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='zachita_konsult',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='zachita_recencirovanie',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='zachita_rukovod_VKR',
        ),
        migrations.RemoveField(
            model_name='groupp',
            name='zachita_uchastie_v_GAK',
        ),
        migrations.AddField(
            model_name='groupp',
            name='amount_of_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название группы: ')),
                ('amount_of_credit', models.IntegerField(default=0)),
                ('kol_stud_budget', models.IntegerField(default=0, verbose_name='Кол. студ.бюджет')),
                ('kol_stud_contract', models.IntegerField(default=0, verbose_name='Кол. студ.контракт')),
                ('obshee_kol_stud', models.IntegerField(default=0, verbose_name='Общее кол.студентов')),
                ('semester', models.IntegerField(default=0, verbose_name='Семестер')),
                ('lekcii_po_ucheb_planu', models.IntegerField(blank=True, null=True, verbose_name='Лекции/ По учебному плану')),
                ('lekcii_zachityvaetsa_v_nagruzku', models.IntegerField(blank=True, null=True, verbose_name='Лекции/ Зачитывается в нагрузку кафедры (ч.)')),
                ('praktZan_po_ucheb_planu', models.IntegerField(blank=True, null=True, verbose_name='Практ.зан/ По учебному плану')),
                ('praktZan_zachityvaetsa_v_nagruzku', models.IntegerField(blank=True, null=True, verbose_name='Практ.зан/ Зачитывается в нагрузку кафедры (ч.)')),
                ('labRab_po_ucheb_planu', models.IntegerField(blank=True, null=True, verbose_name='Лаб.раб/ По учебному плану')),
                ('labRab_zachityvaetsa_v_nagruzku', models.IntegerField(blank=True, null=True, verbose_name='Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)')),
                ('rukovod_KRIKP', models.IntegerField(blank=True, default=0, null=True, verbose_name='Руковод.КРиКП')),
                ('recenzirov_KR', models.IntegerField(blank=True, default=0, null=True, verbose_name='Рецениров_КР')),
                ('priem_SRS', models.FloatField(blank=True, default=0, null=True, verbose_name='Прием СРС')),
                ('praktika_uchebnay', models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Учебная')),
                ('praktika_proizvod', models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Производ')),
                ('praktika_predkval', models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Предквал')),
                ('praktika_pedagog', models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Педагогическая')),
                ('praktika_nauchno', models.IntegerField(blank=True, default=0, null=True, verbose_name='Практика/Научно-исследовательская')),
                ('kontrol_tekuchiy1', models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/текущий (1 контр.точка)')),
                ('kontrol_tekuchiy2', models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/текущий (2 контр.точка)')),
                ('kontrol_tekuchiy3', models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/текущий (3 контр.точка)')),
                ('kontrol_itogovyi', models.FloatField(blank=True, default=0, null=True, verbose_name='Контроль/итоговый (экзамен)')),
                ('zachita_rukovod_VKR', models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ руководство ВКР')),
                ('zachita_konsult', models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ консульт. по разделам')),
                ('zachita_recencirovanie', models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ рецензирование')),
                ('zachita_uchastie_v_GAK', models.FloatField(blank=True, default=0, null=True, verbose_name='Защита вып. квал. работы/ участие в ГАК')),
                ('normokontr', models.FloatField(blank=True, default=0, null=True, verbose_name='Нормоконтр')),
                ('magistratura', models.FloatField(blank=True, default=0, null=True, verbose_name='Магистратура')),
                ('aspirantura_doctorontura', models.FloatField(blank=True, default=0, null=True, verbose_name='Аспирантура, Докторантура')),
                ('online', models.FloatField(blank=True, default=0, null=True, verbose_name='Онлайн')),
                ('offline', models.FloatField(blank=True, default=0, null=True, verbose_name='Офлайн')),
                ('academ_sov', models.FloatField(blank=True, default=0, null=True, verbose_name='Академ. сов.')),
                ('rukovodstvo_kafedroi', models.FloatField(blank=True, default=0, null=True, verbose_name='Руководство кафедрой')),
                ('rukovodstvo_dekanatom', models.FloatField(blank=True, default=0, null=True, verbose_name='Руководство деканатом')),
                ('prochie', models.FloatField(blank=True, default=0, null=True, verbose_name='Прочие')),
                ('vsego_uchebnyh_chasov', models.FloatField(blank=True, default=0, null=True, verbose_name='Всего учебных часов по расчету')),
                ('name_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagr.groupp')),
            ],
        ),
    ]
