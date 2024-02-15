import datetime

from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from api.groupp.forms import GrouppForm
from api.discipline.forms import DisciplineForm
from api.teacher.forms import TeacherForm
from api.nagr.forms import NagruzkaForm
from apps.nagr.models import Nagruzka
from apps.discipline.models import Discipline
from apps.teacher.models import Teacher
from apps.group.models import Groupp
from django.shortcuts import get_object_or_404
import xlwt


def thanks(request):
    return render(request, 'thanks.html',)


def vedomost(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(lekcii_po_ucheb_planu=Sum('teacherr__group_id__lekcii_po_ucheb_planu'),
                                                         lekcii_zachityvaetsa_v_nagruzku=Sum('teacherr__group_id__lekcii_zachityvaetsa_v_nagruzku'),
                                                         praktZan_po_ucheb_planu=Sum('teacherr__group_id__praktZan_po_ucheb_planu'),
                                                         praktZan_zachityvaetsa_v_nagruzku=Sum('teacherr__group_id__praktZan_zachityvaetsa_v_nagruzku'),
                                                         labRab_po_ucheb_planu=Sum('teacherr__group_id__labRab_po_ucheb_planu'),
                                                         labRab_zachityvaetsa_v_nagruzku=Sum('teacherr__group_id__labRab_zachityvaetsa_v_nagruzku'),
                                                         rukovod_KRIKP=Sum('teacherr__group_id__rukovod_KRIKP'),
                                                         recenzirov_KR=Sum('teacherr__group_id__recenzirov_KR'),
                                                         priem_SRS=Sum('teacherr__group_id__priem_SRS'),
                                                         praktika_uchebnay=Sum('teacherr__group_id__praktika_uchebnay'),
                                                         praktika_proizvod=Sum('teacherr__group_id__praktika_proizvod'),
                                                         praktika_predkval=Sum('teacherr__group_id__praktika_predkval'),
                                                         praktika_pedagog=Sum('teacherr__group_id__praktika_pedagog'),
                                                         praktika_nauchno=Sum('teacherr__group_id__praktika_nauchno'),
                                                         kontrol_tekuchiy1=Sum('teacherr__group_id__kontrol_tekuchiy1'),
                                                         kontrol_tekuchiy2=Sum('teacherr__group_id__kontrol_tekuchiy2'),
                                                         kontrol_tekuchiy3=Sum('teacherr__group_id__kontrol_tekuchiy3'),
                                                         kontrol_itogovyii=Sum('teacherr__group_id__kontrol_itogovyi'),
                                                         zachita_rukovod_VKR=Sum('teacherr__group_id__zachita_rukovod_VKR'),
                                                         zachita_konsult=Sum('teacherr__group_id__zachita_konsult'),
                                                         zachita_recencirovanie=Sum('teacherr__group_id__zachita_recencirovanie'),
                                                         zachita_uchastie_v_GAK=Sum('teacherr__group_id__zachita_uchastie_v_GAK'),
                                                         normokontr=Sum('teacherr__group_id__normokontr'),
                                                         magistratura=Sum('teacherr__group_id__magistratura'),
                                                         aspirantura_doctorontura=Sum('teacherr__group_id__aspirantura_doctorontura'),
                                                         online=Sum('teacherr__group_id__online'),
                                                         offline=Sum('teacherr__group_id__offline'),
                                                         academ_sov=Sum('teacherr__group_id__academ_sov'),
                                                         rukovodstvo_kafedroi=Sum('teacherr__group_id__rukovodstvo_kafedroi'),
                                                         rukovodstvo_dekanatom=Sum('teacherr__group_id__rukovodstvo_dekanatom'),
                                                         prochie=Sum('teacherr__group_id__prochie'),
                                                         vsego_uchebnyh_chasov=Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                                        )
        context = {'teachers': teacher}
        return render(request, 'vedomost.html', context)
    

def export_excel(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Наименование дисциплин и других видов работ', 'Количество кредитов', 'Группa',
               'Кол. студ.бюджет', 'Кол. студ.контракт', 'Общее кол.студентов', 'Семестер',
               'Лекции/ По учебному плану', 'Лекции/ Зачитывается в нагрузку кафедры (ч.)',
               'Практ.зан/ По учебному плану', 'Практ.зан/ Зачитывается в нагрузку кафедры (ч.)',
               'Лаб.раб/ По учебному плану', 'Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)',
               'Руковод.КРиКП', 'Рецениров_КР', 'Прием СРС', 'Практика/Учебная', 'Практика/Производ',
               'Практика/Предквал', 'Практика/Педагогическая', 'Практика/Научно-исследовательская',
               'Контроль/текущий (1 контр.точка)', 'Контроль/текущий (2 контр.точка)', 'Контроль/текущий (3 контр.точка)',
               'Контроль/итоговый (экзамен)', 'Защита вып. квал. работы/ руководство ВКР', 'Защита вып. квал. работы/ консульт. по разделам',
               'Защита вып. квал. работы/ рецензирование', 'Защита вып. квал. работы/ участие в ГАК', 'Нормоконтр',
               'Магистратура', 'Аспирантура, Докторантура', 'Онлайн', 'Офлайн', 'Академ. сов.', 'Руководство кафедрой',
               'Руководство деканатом', 'Прочие', 'Всего учебных часов по расчету']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Teacher.objects.filter(id=pk).values_list('teacherr__group_id__discipline_name', 'teacherr__group_id__amount_of_credit',
                                                     'teacherr__group_id__name', 'teacherr__group_id__kol_stud_budget',
                                                     'teacherr__group_id__kol_stud_contract', 'teacherr__group_id__obshee_kol_stud', 'teacherr__group_id__semester',
                                                     'teacherr__group_id__lekcii_po_ucheb_planu', 'teacherr__group_id__lekcii_zachityvaetsa_v_nagruzku',
                                                     'teacherr__group_id__praktZan_po_ucheb_planu', 'teacherr__group_id__praktZan_zachityvaetsa_v_nagruzku',
                                                     'teacherr__group_id__labRab_po_ucheb_planu', 'teacherr__group_id__labRab_zachityvaetsa_v_nagruzku',
                                                     'teacherr__group_id__rukovod_KRIKP', 'teacherr__group_id__recenzirov_KR', 'teacherr__group_id__priem_SRS',
                                                     'teacherr__group_id__praktika_uchebnay', 'teacherr__group_id__praktika_proizvod', 'teacherr__group_id__praktika_predkval',
                                                     'teacherr__group_id__praktika_pedagog', 'teacherr__group_id__praktika_nauchno', 'teacherr__group_id__kontrol_tekuchiy1',
                                                     'teacherr__group_id__kontrol_tekuchiy2', 'teacherr__group_id__kontrol_tekuchiy3', 'teacherr__group_id__kontrol_itogovyi',
                                                     'teacherr__group_id__zachita_rukovod_VKR', 'teacherr__group_id__zachita_konsult', 'teacherr__group_id__zachita_recencirovanie',
                                                     'teacherr__group_id__zachita_uchastie_v_GAK', 'teacherr__group_id__normokontr', 'teacherr__group_id__magistratura',
                                                     'teacherr__group_id__aspirantura_doctorontura', 'teacherr__group_id__online', 'teacherr__group_id__offline',
                                                     'teacherr__group_id__academ_sov', 'teacherr__group_id__rukovodstvo_kafedroi', 'teacherr__group_id__rukovodstvo_dekanatom',
                                                     'teacherr__group_id__prochie', 'teacherr__group_id__vsego_uchebnyh_chasov',

                                                     # # '.', '.', '.', '.', '.', '.',
                                                     # Sum('teacherr__group_id__lekcii_po_ucheb_planu'),
                                                     # Sum('teacherr__group_id__lekcii_zachityvaetsa_v_nagruzku'),
                                                     # Sum('teacherr__group_id__praktZan_po_ucheb_planu'),
                                                     # Sum('teacherr__group_id__praktZan_zachityvaetsa_v_nagruzku'),
                                                     # Sum('teacherr__group_id__labRab_po_ucheb_planu'),
                                                     # Sum('teacherr__group_id__labRab_zachityvaetsa_v_nagruzku'),
                                                     # Sum('teacherr__group_id__rukovod_KRIKP'),
                                                     # Sum('teacherr__group_id__recenzirov_KR'),
                                                     # Sum('teacherr__group_id__priem_SRS'),
                                                     # Sum('teacherr__group_id__praktika_uchebnay'),
                                                     # Sum('teacherr__group_id__praktika_proizvod'),
                                                     # Sum('teacherr__group_id__praktika_predkval'),
                                                     # Sum('teacherr__group_id__praktika_pedagog'),
                                                     # Sum('teacherr__group_id__praktika_nauchno'),
                                                     # Sum('teacherr__group_id__kontrol_itogovyi'),
                                                     # Sum('teacherr__group_id__zachita_rukovod_VKR'),
                                                     # Sum('teacherr__group_id__zachita_konsult'),
                                                     # Sum('teacherr__group_id__zachita_recencirovanie'),
                                                     # Sum('teacherr__group_id__zachita_uchastie_v_GAK'),
                                                     # Sum('teacherr__group_id__normokontr'),
                                                     # Sum('teacherr__group_id__magistratura'),
                                                     # Sum('teacherr__group_id__aspirantura_doctorontura'),
                                                     # Sum('teacherr__group_id__online'),
                                                     # Sum('teacherr__group_id__offline'),
                                                     # Sum('teacherr__group_id__academ_sov'),
                                                     # Sum('teacherr__group_id__rukovodstvo_kafedroi'),
                                                     # Sum('teacherr__group_id__rukovodstvo_dekanatom'),
                                                     # Sum('teacherr__group_id__prochie'),
                                                     # Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                                     )

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


def export_excel_vedomost(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['ФИО', 'Должность', 'Лекции/ По учебному плану', 'Лекции/ Зачитывается в нагрузку кафедры (ч.)',
               'Практ.зан/ По учебному плану', 'Практ.зан/ Зачитывается в нагрузку кафедры (ч.)',
               'Лаб.раб/ По учебному плану', 'Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)',
               'Руковод.КРиКП', 'Рецениров_КР', 'Прием СРС', 'Практика/Учебная', 'Практика/Производ',
               'Практика/Предквал', 'Практика/Педагогическая', 'Практика/Научно-исследовательская',
               'Контроль/итоговый (экзамен)', 'Защита вып. квал. работы/ руководство ВКР', 'Защита вып. квал. работы/ консульт. по разделам',
               'Защита вып. квал. работы/ рецензирование', 'Защита вып. квал. работы/ участие в ГАК', 'Нормоконтр',
               'Магистратура', 'Аспирантура, Докторантура', 'Онлайн', 'Офлайн', 'Академ. сов.', 'Руководство кафедрой',
               'Руководство деканатом', 'Прочие', 'Всего учебных часов по расчету']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Teacher.objects.all().values_list('name', 'job_title', Sum('teacherr__group_id__lekcii_po_ucheb_planu'),
                                             Sum('teacherr__group_id__lekcii_zachityvaetsa_v_nagruzku'), Sum('teacherr__group_id__praktZan_po_ucheb_planu'),
                                             Sum('teacherr__group_id__praktZan_zachityvaetsa_v_nagruzku'), Sum('teacherr__group_id__labRab_po_ucheb_planu'),
                                             Sum('teacherr__group_id__labRab_zachityvaetsa_v_nagruzku'), Sum('teacherr__group_id__rukovod_KRIKP'),
                                             Sum('teacherr__group_id__recenzirov_KR'), Sum('teacherr__group_id__priem_SRS'), Sum('teacherr__group_id__praktika_uchebnay'),
                                             Sum('teacherr__group_id__praktika_proizvod'), Sum('teacherr__group_id__praktika_predkval'), Sum('teacherr__group_id__praktika_pedagog'),
                                             Sum('teacherr__group_id__praktika_nauchno'), Sum('teacherr__group_id__kontrol_itogovyi'), Sum('teacherr__group_id__zachita_rukovod_VKR'),
                                             Sum('teacherr__group_id__zachita_konsult'), Sum('teacherr__group_id__zachita_recencirovanie'), Sum('teacherr__group_id__zachita_uchastie_v_GAK'),
                                             Sum('teacherr__group_id__normokontr'), Sum('teacherr__group_id__magistratura'), Sum('teacherr__group_id__aspirantura_doctorontura'),
                                             Sum('teacherr__group_id__online'), Sum('teacherr__group_id__offline'), Sum('teacherr__group_id__academ_sov'), Sum('teacherr__group_id__rukovodstvo_kafedroi'),
                                             Sum('teacherr__group_id__rukovodstvo_dekanatom'), Sum('teacherr__group_id__prochie'),  Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                             )


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


def createconnects(request):
    if request.method == 'POST':
        form = NagruzkaForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = NagruzkaForm()
    context = {'form': form}
    return render(request, 'createconnects.html', context)


def connectlist(request):
    data = Nagruzka.objects.all()
    context = {'data': data}
    return render(request, 'connectlist.html', context)


def deleteconnect(request, pk):
    data = get_object_or_404(Nagruzka, id=pk)
    data.delete()
    return redirect('/')