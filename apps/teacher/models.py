from django.db import models

# Create your models here.


doljnost = ((1, 'Профессор'),
            (2, 'Доцент'),
            (3, 'Старший преподователь'),
            (4, 'Преподователь'),
            (5, 'зав. лаб.'),
            (6, 'лаборант'),
            (7, 'ст.лаборант'),
            (8, 'инженер'),
            )


class Doljnost(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    stavka = models.IntegerField(verbose_name='Ставка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('-id',)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    is_budget = models.BooleanField(default=False, verbose_name='Бюджет')
    is_not_budget = models.BooleanField(default=False, verbose_name='Не бюджет')
    job_title = models.ForeignKey(Doljnost, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Должность')
    zvanie = models.CharField(max_length=120, verbose_name='Звание')
    ped_staj = models.IntegerField(verbose_name='Пед стаж')
    shtat_sovmest = models.CharField(max_length=250, verbose_name='Штат.или совмест.')
    stavka = models.FloatField(verbose_name='Ставка')
    stavka_budget = models.FloatField(default=0, verbose_name='Ставка для бюджета')

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподователи'
        ordering = ('-id',)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


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

    def get_more_time(self):
        return self.get_time() + 30