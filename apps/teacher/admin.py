from django.contrib import admin
from apps.teacher.models import Teacher, Doljnost
from import_export.admin import ImportExportModelAdmin
from apps.teacher.resources import TeacherResource
from django.utils.html import format_html


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TeacherResource
    list_display = ('get_full_name', 'is_budget', 'job_title', 'get_title_stavka',
                    'zvanie', 'ped_staj', 'shtat_sovmest', 'stavka', 'stavka_budget',
                    'vsego_stavka', 'get_time', 'get_time_budget', 'get_time_vsego',
                    'total_za_vsego_uchebnyh_chasov', 'total_vsego_uchebnyh_chasov_colored',
                    'vsego_colored')
    search_fields = ('first_name', 'last_name')
    list_filter = ('is_budget', 'job_title', )

    def vsego_colored(self, obj):
        if obj.vsego() < obj.get_time_vsego():
            return format_html('<div style="width: 40.33px; height: 31px; background-color: rgba(255, 0, 0, 0.5); color: white; display: flex; align-items: center; justify-content: center;">{}</div>', obj.vsego())
        if obj.vsego() > obj.get_time_vsego() + 150:
            return format_html('<div style="width: 40.33px; height: 31px; background-color: rgba(255, 255, 0, 0.5); color: black; display: flex; align-items: center; justify-content: center;">{}</div>', obj.vsego())
        return format_html('<div style="width: 40.33px; height: 31px; display: flex; align-items: center; justify-content: center;">{}</div>', obj.vsego())

    vsego_colored.short_description = 'Всего'

    def total_vsego_uchebnyh_chasov_colored(self, obj):
        if obj.total_vsego_uchebnyh_chasov() < obj.get_time():
            return format_html('<div style="width: 40.33px; height: 31px; background-color: rgba(255, 0, 0, 0.5); color: white; display: flex; align-items: center; justify-content: center;">{}</div>', obj.total_vsego_uchebnyh_chasov())
        return format_html('<div style="width: 50.33px; height: 31px display: flex; align-items: center; justify-content: center;">{}</div>', obj.total_vsego_uchebnyh_chasov())

    total_vsego_uchebnyh_chasov_colored.short_description = 'Очное'


@admin.register(Doljnost)
class DoljnostAdmin(admin.ModelAdmin):
    list_display = ('name', 'stavka')
    search_fields = ('name', )

