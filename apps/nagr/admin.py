from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.nagr.models import Nagruzka, TeacherSummary
from apps.nagr.resources import TeacherSummaryResource, NagruzkaResource
from django import forms


class NagruzkaForm(forms.ModelForm):
    class Meta:
        model = Nagruzka
        fields = '__all__'
        exclude = ['name']


@admin.register(Nagruzka)
class NagruzkaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = NagruzkaForm
    resource_class = NagruzkaResource
    list_display = ('teacher', 'name', 'discipline_name', 'lekcii_po_ucheb_planu', 'praktZan_po_ucheb_planu',
        'labRab_po_ucheb_planu', 'rukovod_KRIKP', 'recenzirov_KR', 'priem_SRS',
        'praktika_uchebnay', 'praktika_proizvod', 'praktika_predkval',
        'praktika_pedagog', 'praktika_nauchno', 'kontrol_itogovyi', 
        'zachita_rukovod_VKR', 'zachita_konsult', 'zachita_recencirovanie',
        'zachita_uchastie_v_GAK', 'normokontr', 'magistratura',
        'aspirantura_doctorontura', 'academ_sov', 'rukovodstvo_kafedroi',
        'vsego_uchebnyh_chasov', 'za_vsego_uchebnyh_chasov')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name', )
    list_filter = ('teacher', )


@admin.register(TeacherSummary)
class TeacherSummaryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TeacherSummaryResource
    list_display = (
        'teacher', 'get_total_lekcii_po_ucheb_planu', 'get_total_praktZan_po_ucheb_planu',
        'get_total_labRab_po_ucheb_planu', 'get_total_rukovod_KRIKP', 'get_total_recenzirov_KR',
        'get_total_priem_SRS', 'get_total_praktika_uchebnay', 'get_total_praktika_proizvod',
        'get_total_praktika_predkval', 'get_total_praktika_pedagog', 'get_total_praktika_nauchno',
        'get_total_kontrol_itogovyi', 'get_total_zachita_rukovod_VKR', 'get_total_zachita_konsult',
        'get_total_zachita_recencirovanie', 'get_total_zachita_uchastie_v_GAK', 'get_total_normokontr',
        'get_total_magistratura', 'get_total_aspirantura_doctorontura', 'get_total_academ_sov',
        'get_total_rukovodstvo_kafedroi', 'get_total_vsego_uchebnyh_chasov', 'get_total_za_vsego_uchebnyh_chasov',
    )
    search_fields = ('teacher__first_name', 'teacher__last_name')

    def get_total_lekcii_po_ucheb_planu(self, obj):
        return obj.total_lekcii_po_ucheb_planu

    get_total_lekcii_po_ucheb_planu.short_description = 'Лекции'

    def get_total_praktZan_po_ucheb_planu(self, obj):
        return obj.total_praktZan_po_ucheb_planu

    get_total_praktZan_po_ucheb_planu.short_description = 'Практические занятия'

    def get_total_labRab_po_ucheb_planu(self, obj):
        return obj.total_labRab_po_ucheb_planu

    get_total_labRab_po_ucheb_planu.short_description = 'Лабораторные работы'

    def get_total_rukovod_KRIKP(self, obj):
        return obj.total_rukovod_KRIKP

    get_total_rukovod_KRIKP.short_description = 'Руководство КРИКП'

    def get_total_recenzirov_KR(self, obj):
        return obj.total_recenzirov_KR

    get_total_recenzirov_KR.short_description = 'Рецензирование КР'

    def get_total_priem_SRS(self, obj):
        return obj.total_priem_SRS

    get_total_priem_SRS.short_description = 'Прием СРС'

    def get_total_praktika_uchebnay(self, obj):
        return obj.total_praktika_uchebnay

    get_total_praktika_uchebnay.short_description = 'Учебная практика'

    def get_total_praktika_proizvod(self, obj):
        return obj.total_praktika_proizvod

    get_total_praktika_proizvod.short_description = 'Производственная практика'

    def get_total_praktika_predkval(self, obj):
        return obj.total_praktika_predkval

    get_total_praktika_predkval.short_description = 'Предквалификационная практика'

    def get_total_praktika_pedagog(self, obj):
        return obj.total_praktika_pedagog

    get_total_praktika_pedagog.short_description = 'Педагогическая практика'

    def get_total_praktika_nauchno(self, obj):
        return obj.total_praktika_nauchno

    get_total_praktika_nauchno.short_description = 'Научно-исследовательская практика'

    def get_total_kontrol_itogovyi(self, obj):
        return obj.total_kontrol_itogovyi

    get_total_kontrol_itogovyi.short_description = 'Итоговый контроль (экзамен)'

    def get_total_zachita_rukovod_VKR(self, obj):
        return obj.total_zachita_rukovod_VKR

    get_total_zachita_rukovod_VKR.short_description = 'Руководство ВКР'

    def get_total_zachita_konsult(self, obj):
        return obj.total_zachita_konsult

    get_total_zachita_konsult.short_description = 'Консультирование по разделам'

    def get_total_zachita_recencirovanie(self, obj):
        return obj.total_zachita_recencirovanie

    get_total_zachita_recencirovanie.short_description = 'Рецензирование'

    def get_total_zachita_uchastie_v_GAK(self, obj):
        return obj.total_zachita_uchastie_v_GAK

    get_total_zachita_uchastie_v_GAK.short_description = 'Участие в ГАК'

    def get_total_normokontr(self, obj):
        return obj.total_normokontr

    get_total_normokontr.short_description = 'Нормоконтроль'

    def get_total_magistratura(self, obj):
        return obj.total_magistratura

    get_total_magistratura.short_description = 'Магистратура'

    def get_total_aspirantura_doctorontura(self, obj):
        return obj.total_aspirantura_doctorontura

    get_total_aspirantura_doctorontura.short_description = 'Аспирантура, докторантура'

    def get_total_academ_sov(self, obj):
        return obj.total_academ_sov

    get_total_academ_sov.short_description = 'Академический совет'

    def get_total_rukovodstvo_kafedroi(self, obj):
        return obj.total_rukovodstvo_kafedroi

    get_total_rukovodstvo_kafedroi.short_description = 'Руководство кафедрой'

    def get_total_vsego_uchebnyh_chasov(self, obj):
        return obj.total_vsego_uchebnyh_chasov

    get_total_vsego_uchebnyh_chasov.short_description = 'Всего учебных часов'

    def get_total_za_vsego_uchebnyh_chasov(self, obj):
        return obj.total_za_vsego_uchebnyh_chasov

    get_total_za_vsego_uchebnyh_chasov.short_description = 'Всего учебных часов заочно'
