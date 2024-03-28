from django.db import models


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class Settings(SingletonModel):
    s_obshee_kol_stud = models.FloatField()
    
    
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки' 
    
    