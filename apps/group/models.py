from django.db import models
from apps.discipline.models import Discipline

# Create your models here.

select = ((1, 'Очная'),
          (2, 'Заочная'),
          )

sovmes = ((1, 'Совместно'),
          )


class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название группы')
    zaochnoe = models.IntegerField(choices=select, default=1, verbose_name='Форма обучения')
    kol_stud_budget = models.IntegerField(verbose_name='Кол. студ.бюджет', blank=True, null=True)
    kol_stud_contract = models.IntegerField(verbose_name='Кол. студ.контракт', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id', )


class Groupp(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Выберите группу:')
    name = models.CharField(max_length=150, verbose_name='Название группы', blank=True, null=True,)
    zaochnoe = models.IntegerField(choices=select, default=1, verbose_name='Форма обучения')
    for_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплины: ')
    discipline_name = models.CharField(max_length=250, verbose_name='Дисциплины', blank=True, null=True)
    amount_of_credit = models.IntegerField(default=0, verbose_name='Количество кредитов')
    is_kursovoi = models.BooleanField(blank=True, null=True)
    kol_stud_budget = models.IntegerField(verbose_name='Кол. студ.бюджет', blank=True, null=True)
    kol_stud_contract = models.IntegerField(verbose_name='Кол. студ.контракт', blank=True, null=True)
    obshee_kol_stud = models.FloatField(verbose_name='Общее кол.студентов', blank=True, null=True)
    semester = models.IntegerField(verbose_name='Семестер', blank=True, null=True)
    sovmest = models.IntegerField(choices=sovmes, verbose_name='Совместное преподование', blank=True, null=True)
    lekcii_po_ucheb_planu = models.IntegerField(verbose_name='Лекции/ По учебному плану', blank=True, null=True)
    lekcii_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лекции/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)
    praktZan_po_ucheb_planu = models.IntegerField(verbose_name='Практ.зан/ По учебному плану', blank=True, null=True)
    praktZan_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Практ.зан/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)
    labRab_po_ucheb_planu = models.IntegerField(verbose_name='Лаб.раб/ По учебному плану', blank=True, null=True)
    labRab_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)
    rukovod_KRIKP = models.IntegerField(verbose_name='Руковод.КРиКП', blank=True, null=True, default=0)
    recenzirov_KR = models.IntegerField(verbose_name='Рецениров_КР', blank=True, null=True, default=0)
    priem_SRS = models.FloatField(verbose_name='Прием СРС', blank=True, null=True, default=0)
    praktika_uchebnay = models.IntegerField(verbose_name='Практика/Учебная', blank=True, null=True, default=0)
    praktika_proizvod = models.IntegerField(verbose_name='Практика/Производ', blank=True, null=True, default=0)
    praktika_predkval = models.IntegerField(verbose_name='Практика/Предквал', blank=True, null=True, default=0)
    praktika_pedagog = models.IntegerField(verbose_name='Практика/Педагогическая', blank=True, null=True, default=0)
    praktika_nauchno = models.IntegerField(verbose_name='Практика/Научно-исследовательская', blank=True, null=True,default=0)
    kontrol_tekuchiy1 = models.FloatField(verbose_name='Контроль/текущий (1 контр.точка)', blank=True, null=True,default=0)
    kontrol_tekuchiy2 = models.FloatField(verbose_name='Контроль/текущий (2 контр.точка)', blank=True, null=True,default=0)
    kontrol_tekuchiy3 = models.FloatField(verbose_name='Контроль/текущий (3 контр.точка)', default=0, blank=True,null=True, )
    kontrol_itogovyi = models.FloatField(verbose_name='Контроль/итоговый (экзамен)', blank=True, null=True, default=0)
    zachita_rukovod_VKR = models.FloatField(verbose_name='Защита вып. квал. работы/ руководство ВКР', blank=True, null=True, default=0)
    zachita_konsult = models.FloatField(verbose_name='Защита вып. квал. работы/ консульт. по разделам', blank=True,null=True, default=0)
    zachita_recencirovanie = models.FloatField(verbose_name='Защита вып. квал. работы/ рецензирование', blank=True, null=True, default=0)
    zachita_uchastie_v_GAK = models.FloatField(verbose_name='Защита вып. квал. работы/ участие в ГАК', blank=True, null=True, default=0)
    normokontr = models.FloatField(verbose_name='Нормоконтр', blank=True, null=True, default=0)
    magistratura = models.FloatField(verbose_name='Магистратура', blank=True, null=True, default=0)
    aspirantura_doctorontura = models.FloatField(verbose_name='Аспирантура, Докторантура', blank=True, null=True, default=0)
    online = models.FloatField(verbose_name='Онлайн', blank=True, null=True, default=0)
    offline = models.FloatField(verbose_name='Офлайн', blank=True, null=True, default=0)
    academ_sov = models.FloatField(verbose_name='Академ. сов.', blank=True, null=True, default=0)
    rukovodstvo_kafedroi = models.FloatField(verbose_name='Руководство кафедрой', blank=True, null=True, default=0)
    rukovodstvo_dekanatom = models.FloatField(verbose_name='Руководство деканатом', blank=True, null=True, default=0)
    prochie = models.FloatField(verbose_name='Прочие', blank=True, null=True, default=0)
    vsego_uchebnyh_chasov = models.FloatField(verbose_name='Всего учебных часов по расчету', blank=True, null=True, default=0, )
    za_vsego_uchebnyh_chasov = models.FloatField(verbose_name='Заочка Всего учебных часов по расчету', blank=True, null=True, default=0, )

    def __str__(self):
        if self.zaochnoe == 1:
            return f"{self.name}--{self.discipline_name}--{round(self.vsego_uchebnyh_chasov, 1)}"
        else:
            return f"{self.name}--{self.discipline_name}--{round(self.za_vsego_uchebnyh_chasov, 1)}"

    class Meta:
        verbose_name = 'Высчитать нагрузку'
        verbose_name_plural = 'Высчитать нагрузку'
        ordering = ('-id',)
