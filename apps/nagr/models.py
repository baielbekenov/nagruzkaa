from django.db import models
from apps.group.models import Groupp 
from apps.teacher.models import Teacher


# Create your models here.


class Nagruzka(models.Model):
    name = models.CharField(max_length=123, blank=True, null=True)
    group_id = models.ManyToManyField(Groupp, verbose_name='Группа')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacherr', verbose_name='Преподователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нагрузка'
        verbose_name_plural = 'Нагрузки'
    



