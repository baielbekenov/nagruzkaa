from django.db import models
from apps.discipline.models import Discipline

# Create your models here.

select = ((1, 'Очная'),
          (2, 'Заочная'),
          )

sovmes = ((1, 'Совместно'),
          )


class Groupp(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название группы: ')
    zaochnoe = models.IntegerField(choices=select, default=1, verbose_name='Форма обучения')
    for_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплины: ')
    discipline_name = models.CharField(max_length=250, blank=True, null=True)
    amount_of_credit = models.IntegerField(default=0)
    is_kursovoi = models.BooleanField(blank=True, null=True)
    kol_stud_budget = models.IntegerField(verbose_name='Кол. студ.бюджет', blank=True, null=True)
    kol_stud_contract = models.IntegerField(verbose_name='Кол. студ.контракт', blank=True, null=True)
    obshee_kol_stud = models.IntegerField(verbose_name='Общее кол.студентов', blank=True, null=True)
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
        return self.name

    class Meta:
        ordering = ('-id',)


    def obshee_kol_studd(self):
        return self.kol_stud_budget + self.kol_stud_contract


    def rukovod_KRIKPP(self):
        if self.is_kursovoi == True:
            return self.obshee_kol_studd() * 3
        else:
            return 0

    def recenzirov_KRR(self):
        return 0

    def priem_SRSS(self):
        if self.sovmest == 1:
            return 0
        if self.magistraturaa() > 0:
            return 0
        if self.zachita_uchastie_v_GAKK() > 0:
            return 0
        if self.praktika_uchebnayy() > 0:
            return 0
        if self.praktika_proizvodd() > 0:
            return 0
        if self.praktika_pedagogg() > 0:
            return 0
        if self.praktika_nauchnoo() > 0:
            return 0
        if self.praktika_predkvall() > 0:
            return 0
        priem_SRSS = (self.amount_of_credit * 30 - self.lekcii_po_ucheb_planu -
                     self.praktZan_po_ucheb_planu - self.labRab_po_ucheb_planu) / 30 * 0.2 * self.obshee_kol_studd()
        return priem_SRSS

    def praktika_uchebnayy(self):
        if self.discipline_name == 'Учебная практика':
            if self.semester == 4:
                return self.obshee_kol_studd() * 3
            else:
                return 0
        else:
            return 0

    def praktika_proizvodd(self):
        if self.discipline_name == 'Производственная практика':
            if self.semester == 6:
                return self.obshee_kol_studd() * 3
            else:
                return 0
        else:
            return 0

    def praktika_predkvall(self):
        if self.discipline_name == 'Предквалификационная практика':
            if self.semester == 8:
                return self.obshee_kol_studd() * 4
            else:
                return 0
        else:
            return 0

    def praktika_pedagogg(self):
        if self.discipline_name == 'Педагогическая практика':
            if self.semester >= 0:
                return self.obshee_kol_studd() * 16
            else:
                return 0
        else:
            return 0

    def praktika_nauchnoo(self):
        if self.discipline_name == 'Научно-исследовательская практика':
            if self.semester >= 0:
                return self.obshee_kol_studd() * 4
            else:
                return 0
        else:
            return 0

    def kontrol_tekuchiy11(self):
        if self.sovmest == 1:
            return 0
        if self.magistraturaa() > 0:
            return 0
        if self.semester == 0:
            return 0
        if self.praktika_uchebnayy() > 0:
            return 0
        if self.praktika_proizvodd() > 0:
            return 0
        if self.praktika_pedagogg() > 0:
            return 0
        if self.praktika_nauchnoo() > 0:
            return 0
        if self.praktika_predkvall() > 0:
            return 0
        return self.obshee_kol_studd() * 0.3

    def kontrol_tekuchiy22(self):
        if self.sovmest == 1:
            return 0
        if self.magistraturaa() > 0:
            return 0
        if self.semester == 0:
            return 0
        if self.praktika_uchebnayy() > 0:
            return 0
        if self.praktika_proizvodd() > 0:
            return 0
        if self.praktika_pedagogg() > 0:
            return 0
        if self.praktika_nauchnoo() > 0:
            return 0
        if self.praktika_predkvall() > 0:
            return 0
        return self.obshee_kol_studd() * 0.3

    def kontrol_tekuchiy33(self):
        return 0

    def kontrol_itogovyii(self):
        if self.semester == 0:
            return 0
        return self.kontrol_tekuchiy11() + self.kontrol_tekuchiy22() + self.kontrol_tekuchiy33()

    def zachita_rukovod_VKRR(self):
        if self.amount_of_credit == 0:
            if self.discipline_name == 'Защита выпускной квалификационной работы':
                return self.obshee_kol_studd() * 14.5
            else:
                return 0
        else:
            return 0

    def zachita_konsultt(self):
        if self.amount_of_credit == 0:
            if self.discipline_name == 'Защита выпускной квалификационной работы':
                return 0
            else:
                return 0
        else:
            return 0

    def zachita_recencirovaniee(self):
        if self.amount_of_credit == 0:
            if self.discipline_name == 'Защита выпускной квалификационной работы':
                return self.obshee_kol_studd() * 3
            else:
                return 0
        else:
            return 0

    def zachita_uchastie_v_GAKK(self):
        if self.discipline_name == 'Государственный экзамен по направлению потготовки':
            return self.obshee_kol_studd() * 3.5
        if self.discipline_name == 'Защита выпускной квалификационной работы':
            return self.obshee_kol_studd() * 3.5
        else:
            return 0


    def normkontrr(self):
        if self.discipline_name == 'Защита выпускной квалификационной работы':
            if self.zachita_recencirovaniee() > 0:
                return self.obshee_kol_studd() * 1
            else:
                return 0
        else:
            return 0


    def magistraturaa(self):
        if self.discipline_name == 'Руководство магистрских диссертаций':
            return self.obshee_kol_studd() * 25
        else:
            return 0

    def aspirantura_doctoronturaa(self):
        if self.discipline_name == 'Руководство аспирантами, соискателями':
            res = 25+25+75+75+100+150
            return res
        else:
            return 0

    def onlinee(self):
        return 0

    def offlinee(self):
        return 0

    def academ_sovv(self):
        if self.discipline_name == 'Академсоветник':
            return self.obshee_kol_studd() * 1
        else:
            return 0

    def prochiee(self):
        return 0

    def vsego_uchebnyh_chasovv(self):
        if self.zaochnoe == 1:
            res = (self.lekcii_po_ucheb_planu + self.lekcii_zachityvaetsa_v_nagruzku
                                                        + self.praktZan_po_ucheb_planu + self.praktZan_zachityvaetsa_v_nagruzku + self.labRab_po_ucheb_planu
                                                        + self.labRab_zachityvaetsa_v_nagruzku + self.rukovod_KRIKPP() + self.recenzirov_KRR() + self.priem_SRSS()
                                                        + self.praktika_uchebnayy() + self.praktika_proizvodd() + self.praktika_predkvall() + self.praktika_pedagogg()
                                                        + self.praktika_nauchnoo() + self.kontrol_tekuchiy11() + self.kontrol_tekuchiy22() + self.kontrol_tekuchiy33()
                                                        + self.kontrol_itogovyii() + self.zachita_rukovod_VKRR() + self.zachita_konsultt() + self.zachita_recencirovaniee()
                                                        + self.zachita_uchastie_v_GAKK() + self.normkontrr() + self.magistraturaa() + self.aspirantura_doctoronturaa()
                                                        + self.onlinee() + self.offlinee() + self.academ_sovv() + self.rukovodstvo_kafedroi + self.rukovodstvo_dekanatom + self.prochiee()) - self.lekcii_po_ucheb_planu - self.praktZan_po_ucheb_planu - self.labRab_po_ucheb_planu - self.kontrol_tekuchiy11() - self.kontrol_tekuchiy22() - self.kontrol_tekuchiy33()
            return res
        return 0

    def za_vsego_uchebnyh_chasovv(self):
        if self.zaochnoe == 2:
            res = (self.lekcii_po_ucheb_planu + self.lekcii_zachityvaetsa_v_nagruzku
                                                        + self.praktZan_po_ucheb_planu + self.praktZan_zachityvaetsa_v_nagruzku + self.labRab_po_ucheb_planu
                                                        + self.labRab_zachityvaetsa_v_nagruzku + self.rukovod_KRIKPP() + self.recenzirov_KRR() + self.priem_SRSS()
                                                        + self.praktika_uchebnayy() + self.praktika_proizvodd() + self.praktika_predkvall() + self.praktika_pedagogg()
                                                        + self.praktika_nauchnoo() + self.kontrol_tekuchiy11() + self.kontrol_tekuchiy22() + self.kontrol_tekuchiy33()
                                                        + self.kontrol_itogovyii() + self.zachita_rukovod_VKRR() + self.zachita_konsultt() + self.zachita_recencirovaniee()
                                                        + self.zachita_uchastie_v_GAKK() + self.normkontrr() + self.magistraturaa() + self.aspirantura_doctoronturaa()
                                                        + self.onlinee() + self.offlinee() + self.academ_sovv() + self.rukovodstvo_kafedroi + self.rukovodstvo_dekanatom + self.prochiee()) - self.lekcii_po_ucheb_planu - self.praktZan_po_ucheb_planu - self.labRab_po_ucheb_planu - self.kontrol_tekuchiy11() - self.kontrol_tekuchiy22() - self.kontrol_tekuchiy33()
            return res
        return 0