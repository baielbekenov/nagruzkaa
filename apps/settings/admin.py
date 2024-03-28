from django.contrib import admin
from apps.settings.models import Settings


@admin.register(Settings)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('s_obshee_kol_stud', )
    