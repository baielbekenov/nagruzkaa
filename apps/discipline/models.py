from django.db import models

# Create your models here.


class Discipline(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='Название дисциплины: ', unique=True)
    amount_of_credit = models.IntegerField(verbose_name='Количество кредитов')
    is_kursovoi = models.BooleanField(default=False, verbose_name='Курсовой')

    def __str__(self):
        return self.name

    class Meta:
<<<<<<< HEAD
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        ordering = ('-id',)

=======
        ordering = ('-id',)
>>>>>>> c844f21 (ddd)
