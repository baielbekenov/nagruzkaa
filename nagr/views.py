import datetime

from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from nagr.forms import GrouppForm, TeacherForm, ConnectForm, DisciplineForm, GroupForm
from nagr.models import Connect, Teacher, Discipline, Groupp, Group
from django.shortcuts import get_object_or_404
import xlwt


def teacher(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(total=Sum('teacherr__group_id__vsego_uchebnyh_chasov')).order_by('-id')


        context = {'teachers': teacher}
        return render(request, 'teacher.html', context)
    return HttpResponse('Error')


def create(request):
    if request.method == 'POST':
        form = GrouppForm(request.POST)

        if form.is_valid():
            group = form.save(commit=False)
            amount = get_object_or_404(Discipline, id=group.for_discipline_id)
            group.obshee_kol_stud = group.kol_stud_budget + group.kol_stud_contract
            group.amount_of_credit = amount.amount_of_credit
            group.discipline_name = amount.name
            group.is_kursovoi = amount.is_kursovoi
            form.save()
            return redirect('/')
    else:
        form = GrouppForm()
    content = {'form': form}
    return render(request, 'create.html', content)

def create1(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            group_ = form.save(commit=False)
            creategroup = get_object_or_404(Groupp, id=group_.name_id_id)
            group_.name = creategroup.name
            group_.discipline_name = creategroup.discipline_name
            group_.amount_of_credit = creategroup.amount_of_credit
            group_.kol_stud_budget = creategroup.kol_stud_budget
            group_.kol_stud_contract = creategroup.kol_stud_contract
            group_.obshee_kol_stud = creategroup.obshee_kol_stud
            group_.semester = creategroup.semester
            group_.lekcii_po_ucheb_planu = creategroup.lekcii_po_ucheb_planu
            group_.lekcii_zachityvaetsa_v_nagruzku = creategroup.lekcii_zachityvaetsa_v_nagruzku
            group_.praktZan_po_ucheb_planu = creategroup.praktZan_po_ucheb_planu
            group_.praktZan_zachityvaetsa_v_nagruzku = creategroup.praktZan_zachityvaetsa_v_nagruzku
            group_.labRab_po_ucheb_planu = creategroup.labRab_po_ucheb_planu
            group_.labRab_zachityvaetsa_v_nagruzku = creategroup.labRab_zachityvaetsa_v_nagruzku

            if creategroup.is_kursovoi == True:
                group_.rukovod_KRIKP = creategroup.obshee_kol_stud * 3

            if creategroup.lekcii_po_ucheb_planu != 0:
                group_.priem_SRS = (group_.amount_of_credit * 30 - group_.lekcii_po_ucheb_planu - group_.praktZan_po_ucheb_planu - group_.labRab_po_ucheb_planu) / 30 * 0.2 * group_.obshee_kol_stud
                group_.kontrol_tekuchiy1 = creategroup.obshee_kol_stud * 0.3
                group_.kontrol_tekuchiy2 = creategroup.obshee_kol_stud * 0.3
                group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3

            if creategroup.discipline_name == 'Учебная практика':
                if creategroup.semester == 4:
                    group_.priem_SRS = 0
                    group_.praktika_uchebnay = creategroup.obshee_kol_stud * 3
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
            if creategroup.discipline_name == 'Производственная практика':
                if creategroup.semester == 6:
                    group_.priem_SRS = 0
                    group_.praktika_proizvod = creategroup.obshee_kol_stud * 3
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
            if creategroup.discipline_name == 'Предквалификационная практика':
                if creategroup.semester == 8:
                    group_.priem_SRS = 0
                    group_.praktika_predkval = creategroup.obshee_kol_stud * 4
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
            if creategroup.discipline_name == 'Педагогическая практика':
                if creategroup.semester >= 3:
                    group_.priem_SRS = 0
                    group_.praktika_pedagog = creategroup.obshee_kol_stud * 16
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
            if creategroup.discipline_name == 'Научно-исследовательская практика':
                if creategroup.semester >= 6:
                    group_.priem_SRS = 0
                    group_.praktika_nauchno = creategroup.obshee_kol_stud * 4
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
            if creategroup.amount_of_credit == 0:
                if creategroup.discipline_name == 'Руководство кафедрой':
                    group_.rukovodstvo_kafedroi = group_.rukovodstvo_kafedroi
                if creategroup.discipline_name == 'Руководство деканатом':
                    group_.rukovodstvo_dekanatom = group_.rukovodstvo_dekanatom
                if creategroup.discipline_name == 'Академсоветник':
                    group_.academ_sov = creategroup.obshee_kol_stud * 1
                if creategroup.discipline_name == 'Защита выпускной квалификационной работы':
                    group_.priem_SRS = (group_.amount_of_credit * 30 - group_.lekcii_po_ucheb_planu - group_.praktZan_po_ucheb_planu - group_.labRab_po_ucheb_planu) / 30 * 0.2 * group_.obshee_kol_stud
                    group_.kontrol_tekuchiy1 = creategroup.obshee_kol_stud * 0.3
                    group_.kontrol_tekuchiy2 = creategroup.obshee_kol_stud * 0.3
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
                    group_.zachita_rukovod_VKR = creategroup.obshee_kol_stud * 14.5
                    group_.zachita_konsult = 0
                    group_.zachita_recencirovanie = creategroup.obshee_kol_stud * 3
                    group_.zachita_uchastie_v_GAK = creategroup.obshee_kol_stud * 3.5
                    group_.normokontr = creategroup.obshee_kol_stud * 1
                if creategroup.lekcii_po_ucheb_planu == 18:
                    group_.priem_SRS = 0
                    group_.kontrol_tekuchiy1 = creategroup.obshee_kol_stud * 0.3
                    group_.kontrol_tekuchiy2 = creategroup.obshee_kol_stud * 0.3
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
                    group_.zachita_uchastie_v_GAK = creategroup.obshee_kol_stud * 3.5
                if creategroup.discipline_name == 'Руководство магистрских диссертаций':
                    group_.priem_SRS = 0
                    group_.kontrol_tekuchiy1 = 0
                    group_.kontrol_tekuchiy2 = 0
                    group_.kontrol_itogovyi = group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
                    group_.magistratura = creategroup.obshee_kol_stud * 25
                # if creategroup.kol_stud_contract == 0:
                #     if creategroup.semester == 0:
                #         if creategroup.lekcii_po_ucheb_planu == 0:
                #             group_.aspirantura_doctorontura = 25+25+75+75+100+150

            group_.vsego_uchebnyh_chasov = (group_.lekcii_po_ucheb_planu + group_.lekcii_zachityvaetsa_v_nagruzku
                                                    + group_.praktZan_po_ucheb_planu + group_.praktZan_zachityvaetsa_v_nagruzku + group_.labRab_po_ucheb_planu
                                                    + group_.labRab_zachityvaetsa_v_nagruzku + group_.rukovod_KRIKP + group_.recenzirov_KR + group_.priem_SRS
                                                    + group_.praktika_uchebnay + group_.praktika_proizvod + group_.praktika_predkval + group_.praktika_pedagog
                                                    + group_.praktika_nauchno + group_.kontrol_tekuchiy1 + group_.kontrol_tekuchiy2 + group_.kontrol_tekuchiy3
                                                    + group_.kontrol_itogovyi + group_.zachita_rukovod_VKR + group_.zachita_konsult + group_.zachita_recencirovanie
                                                    + group_.zachita_uchastie_v_GAK + group_.normokontr + group_.magistratura + group_.aspirantura_doctorontura
                                                    + group_.online + group_.offline + group_.academ_sov + group_.rukovodstvo_kafedroi + group_.rukovodstvo_dekanatom + group_.prochie) - group_.lekcii_po_ucheb_planu - group_.praktZan_po_ucheb_planu - group_.labRab_po_ucheb_planu - group_.kontrol_tekuchiy1 - group_.kontrol_tekuchiy2 - group_.kontrol_tekuchiy3

            form.save()
            return redirect('/')
    else:
        form = GroupForm()
    content = {'form': form}
    return render(request, 'create1.html', content)


def group_teacher(request, pk):
    if request.method == 'GET':
        teacher = Teacher.objects.filter(id=pk).annotate(lekcii_po_ucheb_planu=Sum('teacherr__group_id__lekcii_po_ucheb_planu'),
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
                                                         kontrol_itogovyi=Sum('teacherr__group_id__kontrol_itogovyi'),
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


        context = {'teachers': teacher,}
        return render(request, 'group_teacher.html', context)
    return HttpResponse('Error')

def creatediscipline(request):
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = DisciplineForm()

    context = {'form': form}
    return render(request, 'creatediscipline.html', context)


def thanks(request):
    return render(request, 'thanks.html',)

def createteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            # if teacher.name == teacher.name:
            #     if teacher.is_budget == teacher.is_budget:
            #         if teacher.job_title == teacher.job_title:
            #             return HttpResponse('Преподователь уже в базе!')
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'createteacher.html', context)

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
                                                         kontrol_itogovyi=Sum('teacherr__group_id__kontrol_itogovyi'),
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
        form = ConnectForm(request.POST)
        if form.is_valid():
            connect = form.save(commit=False)
            teacher = get_object_or_404(Teacher, id=connect.teacher_id)
            group = get_object_or_404(Group, id=connect.group_id_id)
            # connect.name = teacher.name
            # connect.job_title = teacher.job_title
            # connect.zvanie = teacher.zvanie
            # connect.ped_staj = teacher.ped_staj
            # connect.shtat_sovmest = teacher.shtat_sovmest
            # connect.shtat_edinicy_budget = teacher.stavka_budget
            # connect.shtat_edinicy_kontrakt_ochnoe = teacher.stavka_ochnoe
            # connect.shtat_edinicy_kontrakt_zaochnoe = 0
            # connect.shtat_edinicy_vsego = teacher.stavka_budget + teacher.stavka_ochnoe + 0
            # if teacher.is_budget == True:
            #     connect.ucheb_nagruzka_budget = group.Sum('teacherr__group_id__vsego_uchebnyh_chasov')
            # else:
            #     connect.ucheb_nagruzka_kontract_ochnoe = group.Sum('teacherr__group_id__vsego_uchebnyh_chasov')
            # connect.ucheb_nagruzka_kontract_zaochnoe = 0
            # connect.ucheb_nagruzka_Vsego = group.Sum('teacherr__group_id__vsego_uchebnyh_chasov')

            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = ConnectForm()
    context = {'form': form}
    return render(request, 'createconnects.html', context)

def shtatnoe(request):
    connect = Connect.objects.all()
    context = {'connects': connect}
    return render(request, 'shtatnoe.html', context)


def showgroupp(request):
    if request.method == 'GET':
        groupp = Group.objects.all()

        context = {'groupp': groupp}
        return render(request, 'showgroupp.html', context)