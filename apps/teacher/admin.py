from django.contrib import admin
from apps.teacher.models import Teacher, Doljnost


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_budget', 'is_not_budget', 'job_title',
                    'zvanie', 'ped_staj', 'shtat_sovmest', 'stavka', 'stavka_budget')
    search_fields = ('first_name', 'last_name')


@admin.register(Doljnost)
class DoljnostAdmin(admin.ModelAdmin):
    list_display = ('name', 'stavka')
    search_fields = ('name', )

