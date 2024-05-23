from django.db import models


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Settings(SingletonModel):
    s_obshee_kol_stud = models.FloatField("Значение для * Общее кол.студентов")
    recenzirov_kr = models.FloatField("Значение для * Рецениров_КР")
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки' 
    
    