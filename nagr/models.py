from django.db import models


# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='Название дисциплины: ', unique=True)
    amount_of_credit = models.IntegerField(verbose_name='Количество кредитов')
    is_kursovoi = models.BooleanField(default=False, verbose_name='Курсовой')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


doljnost = ((1, 'Профессор'),
            (2, 'Доцент'),
            (3, 'Старший преподователь'),
            (4, 'Преподователь')
            )


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    is_budget = models.BooleanField(default=False, verbose_name='Бюджетный')
    job_title = models.IntegerField(choices=doljnost, verbose_name='Должность')
    zvanie = models.CharField(max_length=120, verbose_name='Звание')
    ped_staj = models.IntegerField(verbose_name='Пед стаж')
    shtat_sovmest = models.CharField(max_length=250, verbose_name='Штат.или совмест.')
    stavka = models.FloatField(verbose_name='Ставка')
    zaochnoe_stavka = models.FloatField(default=0, verbose_name='Заочная ставка', blank=True, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_vsego_stavok(self):
        return self.stavka + self.zaochnoe_stavka

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_title_stavka(self):
        if self.job_title == 1:
            return 750
        if self.job_title == 2:
            return 800
        if self.job_title == 3:
            return 850
        if self.job_title == 4:
            return 860

    def get_null(self):
        return 0

    def get_time(self):
        if self.job_title == 1:
            return self.stavka * 750
        if self.job_title == 2:
            return self.stavka * 800
        if self.job_title == 3:
            return self.stavka * 850
        if self.job_title == 4:
            return  self.stavka * 860


    def get_time_zaochnoe(self):
        if self.job_title == 1:
            return self.zaochnoe_stavka * 750
        if self.job_title == 2:
            return self.zaochnoe_stavka * 800
        if self.job_title == 3:
            return self.zaochnoe_stavka * 850
        if self.job_title == 4:
            return  self.zaochnoe_stavka * 860




class Groupp(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название группы: ')
    for_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплины: ')
    discipline_name = models.CharField(max_length=250, blank=True, null=True)
    amount_of_credit = models.IntegerField(default=0)
    is_kursovoi = models.BooleanField(blank=True, null=True)
    kol_stud_budget = models.IntegerField(verbose_name='Кол. студ.бюджет', blank=True, null=True)
    kol_stud_contract = models.IntegerField(verbose_name='Кол. студ.контракт', blank=True, null=True)
    obshee_kol_stud = models.IntegerField(verbose_name='Общее кол.студентов', blank=True, null=True)
    semester = models.IntegerField(verbose_name='Семестер', blank=True, null=True)
    lekcii_po_ucheb_planu = models.IntegerField(verbose_name='Лекции/ По учебному плану', blank=True, null=True)
    lekcii_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лекции/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)
    praktZan_po_ucheb_planu = models.IntegerField(verbose_name='Практ.зан/ По учебному плану', blank=True, null=True)
    praktZan_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Практ.зан/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)
    labRab_po_ucheb_planu = models.IntegerField(verbose_name='Лаб.раб/ По учебному плану', blank=True, null=True)
    labRab_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


class Group(models.Model):
    name_id = models.ForeignKey(Groupp, on_delete=models.CASCADE, verbose_name='Выберите группу')
    name = models.CharField(max_length=150, verbose_name='Название группы: ', blank=True, null=True)
    discipline_name = models.CharField(max_length=250, blank=True, null=True)
    zaochnoe = models.BooleanField(default=False)
    amount_of_credit = models.IntegerField(default=0)
    kol_stud_budget = models.IntegerField(verbose_name='Кол. студ.бюджет', default=0)
    kol_stud_contract = models.IntegerField(verbose_name='Кол. студ.контракт', default=0)
    obshee_kol_stud = models.IntegerField(verbose_name='Общее кол.студентов', default=0)
    semester = models.IntegerField(verbose_name='Семестер', default=0)
    lekcii_po_ucheb_planu = models.IntegerField(verbose_name='Лекции/ По учебному плану', blank=True, null=True, default=0)
    lekcii_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лекции/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True, default=0)
    praktZan_po_ucheb_planu = models.IntegerField(verbose_name='Практ.зан/ По учебному плану', blank=True, null=True, default=0)
    praktZan_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Практ.зан/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True, default=0)
    labRab_po_ucheb_planu = models.IntegerField(verbose_name='Лаб.раб/ По учебному плану', blank=True, null=True, default=0)
    labRab_zachityvaetsa_v_nagruzku = models.IntegerField(verbose_name='Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)', blank=True, null=True, default=0)
    rukovod_KRIKP = models.IntegerField(verbose_name='Руковод.КРиКП', blank=True, null=True, default=0)
    recenzirov_KR = models.IntegerField(verbose_name='Рецениров_КР', blank=True, null=True, default=0)
    priem_SRS = models.FloatField(verbose_name='Прием СРС', blank=True, null=True, default=0 )
    praktika_uchebnay = models.IntegerField(verbose_name='Практика/Учебная', blank=True, null=True, default=0)
    praktika_proizvod = models.IntegerField(verbose_name='Практика/Производ', blank=True, null=True, default=0)
    praktika_predkval = models.IntegerField(verbose_name='Практика/Предквал',  blank=True, null=True, default=0)
    praktika_pedagog = models.IntegerField(verbose_name='Практика/Педагогическая',  blank=True, null=True, default=0)
    praktika_nauchno = models.IntegerField(verbose_name='Практика/Научно-исследовательская',  blank=True, null=True, default=0)
    kontrol_tekuchiy1 = models.FloatField(verbose_name='Контроль/текущий (1 контр.точка)', blank=True, null=True, default=0)
    kontrol_tekuchiy2 = models.FloatField(verbose_name='Контроль/текущий (2 контр.точка)', blank=True, null=True, default=0)
    kontrol_tekuchiy3 = models.FloatField(verbose_name='Контроль/текущий (3 контр.точка)', default=0, blank=True, null=True, )
    kontrol_itogovyi = models.FloatField(verbose_name='Контроль/итоговый (экзамен)', blank=True, null=True, default=0)
    zachita_rukovod_VKR = models.FloatField(verbose_name='Защита вып. квал. работы/ руководство ВКР', blank=True, null=True, default=0)
    zachita_konsult = models.FloatField(verbose_name='Защита вып. квал. работы/ консульт. по разделам', blank=True, null=True, default=0)
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
    vsego_uchebnyh_chasov = models.FloatField(verbose_name='Всего учебных часов по расчету', blank=True, null=True, default=0,)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_vsego_ucheb_chasov(self):
        if self.zaochnoe == True:
            count = []
            count.append(self.vsego_uchebnyh_chasov)
            kol = len(count)
            total = 0
            for i in range(0, kol):
                total += i
            return total
        else:
            return 0



class Connect(models.Model):
    group_id = models.ManyToManyField(Group, verbose_name='Группа')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacherr', verbose_name='Преподователь')

    def __str__(self):
        return f'{self.teacher} --> {self.group_id.name}'



