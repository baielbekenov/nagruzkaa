from django.db import models
from apps.group.models import Groupp 
from apps.teacher.models import Teacher


# Create your models here.


class Nagruzka(models.Model):
    group_id = models.ManyToManyField(Groupp, verbose_name='Группа')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacherr', verbose_name='Преподователь')

    def __str__(self):
        return self.teacher
    



