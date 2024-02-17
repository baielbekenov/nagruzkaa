# Generated by Django 4.1.2 on 2022-10-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('amount_of_credit', models.IntegerField(verbose_name='Количество кредитов')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_budget', models.BooleanField(verbose_name='Бюджетный')),
            ],
        ),
        migrations.CreateModel(
            name='Groupp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('kol_stud_budget', models.IntegerField(blank=True, null=True, verbose_name='Кол. студ.бюджет')),
                ('kol_stud_contract', models.IntegerField(blank=True, null=True, verbose_name='Кол. студ.контракт')),
                ('obshee_kol_stud', models.IntegerField(blank=True, null=True, verbose_name='Общее кол.студентов')),
                ('semester', models.IntegerField(blank=True, null=True, verbose_name='Семестер')),
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
                ('for_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nagr.discipline', verbose_name='Дисциплина')),
            ],
        ),
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_id', models.ManyToManyField(to='nagr.discipline')),
                ('group_id', models.ManyToManyField(to='nagr.groupp')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacherr', to='nagr.teacher')),
            ],
        ),
    ]