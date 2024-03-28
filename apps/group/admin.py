from django.contrib import admin
from apps.group.models import Groupp, Group
from import_export.admin import ImportExportModelAdmin
from apps.settings.models import Settings


# Register your models here.

settings_record = Settings.objects.first()
s_obshee_kol_stud = settings_record.s_obshee_kol_stud

@admin.register(Groupp)
class GrouppAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('discipline_name', 'name', 'vsego_uchebnyh_chasov', 'kol_stud_budget', 'kol_stud_contract', 'obshee_kol_stud', 'semester',
                    'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku', 'praktZan_po_ucheb_planu',
                    'praktZan_zachityvaetsa_v_nagruzku', 'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku', 
                    'rukovod_KRIKP', 'recenzirov_KR', 'priem_SRS', 'praktika_uchebnay', 
                    'praktika_proizvod', 'praktika_predkval', 'praktika_pedagog', 'praktika_nauchno',
                    'kontrol_tekuchiy1', 'kontrol_tekuchiy2', 'kontrol_tekuchiy3', 'kontrol_itogovyi',
                    'zachita_rukovod_VKR', 'zachita_konsult', 'zachita_recencirovanie', 'zachita_uchastie_v_GAK',
                    'normokontr', 'magistratura', 'aspirantura_doctorontura', 'online', 'offline', 'academ_sov',
                    'rukovodstvo_kafedroi', 'rukovodstvo_dekanatom', 'prochie', 'vsego_uchebnyh_chasov')

    list_filter = ('discipline_name', 'name')

    def lekcii_zachityvaetsa_v_nagruzku(self, obj):
        # Возвращает первые 50 символов поля description
        return obj.lekcii_zachityvaetsa_v_nagruzku[:5]

    lekcii_zachityvaetsa_v_nagruzku.short_description = 'кол'

    fields = ['group', 'for_discipline', 'semester', 'sovmest',
              'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku',
              'praktZan_po_ucheb_planu', 'praktZan_zachityvaetsa_v_nagruzku',
              'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku',
              'rukovodstvo_kafedroi', 'rukovodstvo_dekanatom']

    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        # Проверяем, выбрана ли группа
        if obj.group:
            # Автоматически заполняем поля из выбранной группы
            obj.name = obj.group.name
            obj.zaochnoe = obj.group.zaochnoe
            obj.kol_stud_budget = obj.group.kol_stud_budget
            obj.kol_stud_contract = obj.group.kol_stud_contract
            obj.obshee_kol_stud = (obj.group.kol_stud_budget + obj.group.kol_stud_contract) * s_obshee_kol_stud
            print('s_obshee_kol_stud: ', s_obshee_kol_stud)
            super().save_model(request, obj, form, change)

        # Проверяем, выбрана ли дисциплина
        if obj.for_discipline:
            # Автоматически заполняем название дисциплины
            obj.discipline_name = obj.for_discipline.name
            obj.amount_of_credit = obj.for_discipline.amount_of_credit
            obj.is_kursovoi = obj.for_discipline.is_kursovoi
            super().save_model(request, obj, form, change)

        def rukovod_KRIKP():
            if obj.is_kursovoi == True:
                return obj.obshee_kol_stud * 3
            else:
                return 0
        obj.rukovod_KRIKP = rukovod_KRIKP()

        obj.recenzirov_KRR = 0

        def priem_SRS():
            if obj.sovmest == 1:
                return 0
            if obj.magistraturaa() > 0:
                return 0
            if obj.zachita_uchastie_v_GAKK() > 0:
                return 0
            if obj.praktika_uchebnayy() > 0:
                return 0
            if obj.praktika_proizvodd() > 0:
                return 0
            if obj.praktika_predkval > 0:
                return 0
            if obj.praktika_pedagogg() > 0:
                return 0
            if obj.praktika_nauchnoo() > 0:
                return 0
            if obj.praktika_predkvall() > 0:
                return 0
            priem_SRS = (obj.amount_of_credit * 30 - obj.lekcii_po_ucheb_planu -
                          obj.praktZan_po_ucheb_planu - obj.labRab_po_ucheb_planu) / 30 * 0.2 * obj.obshee_kol_studd()
            return priem_SRS

        obj.priem_SRS = priem_SRS()

        def praktika_uchebnay():
            if obj.discipline_name == 'Учебная практика':
                if obj.semester == 4 or obj.semester == 3:
                    return obj.obshee_kol_stud * 3
                else:
                    return 0
            else:
                return 0
        obj.praktika_uchebnay = praktika_uchebnay()

        def praktika_proizvod():
            if obj.discipline_name == 'Производственная практика':
                if obj.semester == 6 or obj.semester == 5:
                    return obj.obshee_kol_stud * 3
                else:
                    return 0
            else:
                return 0
        obj.praktika_proizvod = praktika_proizvod()

        def praktika_predkval():
            if obj.discipline_name == 'Предквалификационная практика':
                if obj.semester == 8 or obj.semester == 7:
                    return obj.obshee_kol_stud * 4
                else:
                    return 0
            else:
                return 0
        obj.praktika_predkval = praktika_predkval()

        def praktika_pedagog():
            if obj.discipline_name == 'Педагогическая практика':
                if obj.semester >= 0:
                    return obj.obshee_kol_stud * 16
                else:
                    return 0
            else:
                return 0
        obj.praktika_pedagog = praktika_pedagog()

        def praktika_nauchno():
            if obj.discipline_name == 'Научно-исследовательская практика':
                if obj.semester >= 0:
                    return obj.obshee_kol_stud * 4
                else:
                    return 0
            else:
                return 0
        obj.praktika_nauchno = praktika_nauchno()

        def kontrol_tekuchiy1():
            if obj.sovmest == 1:
                return 0
            if obj.magistratura > 0:
                return 0
            if obj.semester == 0:
                return 0
            if obj.praktika_uchebnay > 0:
                return 0
            if obj.praktika_proizvod > 0:
                return 0
            if obj.praktika_pedagog > 0:
                return 0
            if obj.praktika_nauchno > 0:
                return 0
            if obj.praktika_predkval > 0:
                return 0
            if obj.discipline_name == 'Академсоветник':
                return 0
            if obj.labRab_po_ucheb_planu == 64:
                return obj.obshee_kol_stud * 0.1
            return obj.obshee_kol_stud * 0.3
        obj.kontrol_tekuchiy1 = kontrol_tekuchiy1()

        def kontrol_tekuchiy2():
            if obj.sovmest == 1:
                return 0
            if obj.magistratura > 0:
                return 0
            if obj.semester == 0:
                return 0
            if obj.praktika_uchebnay > 0:
                return 0
            if obj.praktika_proizvod > 0:
                return 0
            if obj.praktika_pedagog > 0:
                return 0
            if obj.praktika_nauchno > 0:
                return 0
            if obj.praktika_predkval > 0:
                return 0
            if obj.discipline_name == 'Академсоветник':
                return 0
            if obj.labRab_po_ucheb_planu == 64:
                return obj.obshee_kol_stud * 0.1
            return obj.obshee_kol_stud * 0.3
        obj.kontrol_tekuchiy2 = kontrol_tekuchiy2()

        def kontrol_tekuchiy3():
            return 0
        obj.kontrol_tekuchiy3 = kontrol_tekuchiy3()

        def kontrol_itogovyi():
            if obj.semester == 0:
                return 0
            return obj.kontrol_tekuchiy1 + obj.kontrol_tekuchiy2 + obj.kontrol_tekuchiy3
        obj.kontrol_itogovyi = kontrol_itogovyi()

        def zachita_rukovod_VKR():
            if obj.amount_of_credit == 0:
                if obj.discipline_name == 'Защита выпускной квалификационной работы':
                    return obj.obshee_kol_stud * 14.5
                else:
                    return 0
            else:
                return 0
        obj.zachita_rukovod_VKR = zachita_rukovod_VKR()

        def zachita_konsult():
            if obj.amount_of_credit == 0:
                if obj.discipline_name == 'Защита выпускной квалификационной работы':
                    return 0
                else:
                    return 0
            else:
                return 0
        obj.zachita_konsult = zachita_konsult()

        def zachita_recencirovanie():
            if obj.amount_of_credit == 0:
                if obj.discipline_name == 'Защита выпускной квалификационной работы':
                    return obj.obshee_kol_stud * 3
                else:
                    return 0
            else:
                return 0
        obj.zachita_recencirovanie = zachita_recencirovanie()

        def zachita_uchastie_v_GAK():
            if obj.discipline_name == 'Государственный экзамен по направлению потготовки':
                return obj.obshee_kol_stud * 3.5
            if obj.discipline_name == 'Защита выпускной квалификационной работы':
                return obj.obshee_kol_stud * 3.5
            else:
                return 0
        obj.zachita_uchastie_v_GAK = zachita_uchastie_v_GAK()

        def normkontr():
            if obj.discipline_name == 'Защита выпускной квалификационной работы':
                if obj.zachita_recencirovanie > 0:
                    return obj.obshee_kol_stud * 1
                else:
                    return 0
            else:
                return 0
        obj.normkontr = normkontr()

        def magistratura():
            if obj.discipline_name == 'Руководство магистрских диссертаций':
                return obj.obshee_kol_stud * 25
            else:
                return 0
        obj.magistratura = magistratura()

        # Не законченная логика
        def aspirantura_doctorontura():
            if obj.discipline_name == 'Руководство аспирантами, соискателями':
                res = 25 + 25 + 75 + 75 + 100 + 150
                return res
            else:
                return 0
        obj.aspirantura_doctorontura = aspirantura_doctorontura()

        def online():
            return 0
        obj.online = online()

        def offline():
            return 0
        obj.offline = offline()

        def academ_sov():
            if obj.discipline_name == 'Академсоветник':
                return obj.obshee_kol_stud * 1
            else:
                return 0
        obj.academ_sov = academ_sov()

        def prochie():
            return 0
        obj.prochie = prochie()

        def vsego_uchebnyh_chasov():
            if obj.zaochnoe == 1:
                res = (obj.lekcii_po_ucheb_planu + obj.lekcii_zachityvaetsa_v_nagruzku
                       + obj.praktZan_po_ucheb_planu + obj.praktZan_zachityvaetsa_v_nagruzku + obj.labRab_po_ucheb_planu
                       + obj.labRab_zachityvaetsa_v_nagruzku + obj.rukovod_KRIKP + obj.recenzirov_KR + obj.priem_SRS
                       + obj.praktika_uchebnay + obj.praktika_proizvod + obj.praktika_predkval + obj.praktika_pedagog
                       + obj.praktika_nauchno + obj.kontrol_tekuchiy1 + obj.kontrol_tekuchiy2 + obj.kontrol_tekuchiy3
                       + obj.kontrol_itogovyi + obj.zachita_rukovod_VKR + obj.zachita_konsult + obj.zachita_recencirovanie
                       + obj.zachita_uchastie_v_GAK + obj.normkontr + obj.magistratura + obj.aspirantura_doctorontura
                       + obj.online + obj.offline + obj.academ_sov + obj.rukovodstvo_kafedroi + obj.rukovodstvo_dekanatom + obj.prochie) - obj.lekcii_po_ucheb_planu - obj.praktZan_po_ucheb_planu - obj.labRab_po_ucheb_planu - obj.kontrol_tekuchiy1 - obj.kontrol_tekuchiy2 - obj.kontrol_tekuchiy3
                return res
            return 0
        obj.vsego_uchebnyh_chasov = vsego_uchebnyh_chasov()

        def za_vsego_uchebnyh_chasov():
            if obj.zaochnoe == 2:
                res = (obj.lekcii_po_ucheb_planu + obj.lekcii_zachityvaetsa_v_nagruzku
                       + obj.praktZan_po_ucheb_planu + obj.praktZan_zachityvaetsa_v_nagruzku + obj.labRab_po_ucheb_planu
                       + obj.labRab_zachityvaetsa_v_nagruzku + obj.rukovod_KRIKP + obj.recenzirov_KR + obj.priem_SRS
                       + obj.praktika_uchebnay + obj.praktika_proizvod + obj.praktika_predkval + obj.praktika_pedagog
                       + obj.praktika_nauchno + obj.kontrol_tekuchiy1 + obj.kontrol_tekuchiy2 + obj.kontrol_tekuchiy3
                       + obj.kontrol_itogovyi + obj.zachita_rukovod_VKR + obj.zachita_konsult + obj.zachita_recencirovanie
                       + obj.zachita_uchastie_v_GAK + obj.normkontr + obj.magistratura + obj.aspirantura_doctorontura
                       + obj.online + obj.offline + obj.academ_sov + obj.rukovodstvo_kafedroi + obj.rukovodstvo_dekanatom + obj.prochie) - obj.lekcii_po_ucheb_planu - obj.praktZan_po_ucheb_planu - obj.labRab_po_ucheb_planu - obj.kontrol_tekuchiy1 - obj.kontrol_tekuchiy2 - obj.kontrol_tekuchiy3
                return res
            return 0
        obj.za_vsego_uchebnyh_chasov = za_vsego_uchebnyh_chasov()


        super().save_model(request, obj, form, change)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'zaochnoe', 'kol_stud_budget', 'kol_stud_contract')
