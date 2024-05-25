from django.db import models


class Doljnost(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    stavka = models.IntegerField(verbose_name='Количество часов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('-id',)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    job_title = models.ForeignKey(Doljnost, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Должность')
    zvanie = models.CharField(max_length=120, verbose_name='Звание')
    ped_staj = models.IntegerField(verbose_name='Пед стаж')
    shtat_sovmest = models.CharField(max_length=250, verbose_name='Штат.или совмест.')
    is_budget = models.BooleanField(default=False, verbose_name='Бюджет')
    stavka_budget = models.FloatField(default=0, verbose_name='Ставка для бюджета')
    stavka = models.FloatField(verbose_name='Ставка')


    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'
        ordering = ('id',)

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.get_full_name()

    get_full_name.short_description = 'Ф.И.О преподавателя'

    def get_title_stavka(self):
        if self.job_title.id == 1:
            return 750
        if self.job_title.id == 2:
            return 800
        if self.job_title.id == 3:
            return 850
        if self.job_title.id == 4:
            return 860

    get_title_stavka.short_description = 'Часы по должности'

    def vsego_stavka(self):
        return self.stavka_budget + self.stavka

    vsego_stavka.short_description = 'Всего ставка'

    def get_time(self):
        if self.job_title.id == 1:
            return self.stavka * 750
        if self.job_title.id == 2:
            return self.stavka * 800
        if self.job_title.id == 3:
            return self.stavka * 850
        if self.job_title.id == 4:
            return  self.stavka * 860
        return 0

    get_time.short_description = 'Необходимые часы'

    def get_time_budget(self):
        if self.job_title.id == 1:
            return self.stavka_budget * 750
        if self.job_title.id == 2:
            return self.stavka_budget * 800
        if self.job_title.id == 3:
            return self.stavka_budget * 850
        if self.job_title.id == 4:
            return  self.stavka_budget * 860
        return 0

    get_time_budget.short_description = 'Необходимые часы бюджет'

    def get_time_vsego(self):
        return self.get_time() + self.get_time_budget()

    get_time_vsego.short_description = 'Всего часы'

    def total_vsego_uchebnyh_chasov(self):
        nagruzki = self.teacherr.all()
        total_hours = sum(nagruzka.group_id.vsego_uchebnyh_chasov for nagruzka in nagruzki if nagruzka.group_id and nagruzka.group_id.vsego_uchebnyh_chasov is not None)
        return round(total_hours, 1)

    total_vsego_uchebnyh_chasov.short_description = 'Очное'

    def total_za_vsego_uchebnyh_chasov(self):
        nagruzki = self.teacherr.all()
        total_hours = sum(nagruzka.group_id.za_vsego_uchebnyh_chasov for nagruzka in nagruzki if nagruzka.group_id and nagruzka.group_id.za_vsego_uchebnyh_chasov is not None)
        return round(total_hours, 1)

    total_za_vsego_uchebnyh_chasov.short_description = 'Заочное'

    def vsego(self):
        return round(self.total_vsego_uchebnyh_chasov() + self.total_za_vsego_uchebnyh_chasov(), 1)

    vsego.short_description = 'Всего'
