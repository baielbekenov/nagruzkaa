from django.contrib import admin
from apps.discipline.models import Discipline

# Register your models here.

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount_of_credit', 'is_kursovoi')
    search_fields = ('name', )
    