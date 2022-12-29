import datetime

from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from nagr.forms import GrouppForm, TeacherForm, ConnectForm, DisciplineForm
from nagr.models import Connect, Teacher, Discipline, Groupp
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
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
            group.obshee_kol_stud = group.obshee_kol_studd()
            group.amount_of_credit = amount.amount_of_credit
            group.discipline_name = amount.name
            group.is_kursovoi = amount.is_kursovoi
            group.rukovod_KRIKP = group.rukovod_KRIKPP()
            group.recenzirov_KR = group.recenzirov_KRR()
            group.priem_SRS = group.priem_SRSS()
            group.praktika_uchebnay = group.praktika_uchebnayy()
            group.praktika_proizvod = group.praktika_proizvodd()
            group.praktika_predkval = group.praktika_predkvall()
            group.praktika_pedagog = group.praktika_pedagogg()
            group.praktika_nauchno = group.praktika_nauchnoo()
            group.kontrol_tekuchiy1 = group.kontrol_tekuchiy11()
            group.kontrol_tekuchiy2 = group.kontrol_tekuchiy22()
            group.kontrol_tekuchiy3 = group.kontrol_tekuchiy33()
            group.kontrol_itogovyi = group.kontrol_itogovyii()
            group.zachita_rukovod_VKR = group.zachita_rukovod_VKRR()
            group.zachita_konsult = group.zachita_konsultt()
            group.zachita_recencirovanie = group.zachita_recencirovaniee()
            group.zachita_uchastie_v_GAK = group.zachita_uchastie_v_GAKK()
            group.normokontr = group.normkontrr()
            group.magistratura = group.magistraturaa()
            group.aspirantura_doctorontura = group.aspirantura_doctoronturaa()
            group.online = group.onlinee()
            group.offline = group.offlinee()
            group.academ_sov = group.academ_sovv()
            group.prochie = group.prochiee()
            group.vsego_uchebnyh_chasov = group.vsego_uchebnyh_chasovv()
            group.za_vsego_uchebnyh_chasov = group.za_vsego_uchebnyh_chasovv()


            form.save()
            return redirect('teacher')
    else:
        form = GrouppForm()
    content = {'form': form}
    return render(request, 'create.html', content)

def deletegroup(request, pk):
    group = get_object_or_404(Groupp, id=pk)
    group.delete()
    return redirect('showgroup')


def showgroup(request):
    group = Groupp.objects.all()
    context = {'groups': group}
    return render(request, 'showgroup.html', context)

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

def disciplinelist(request):
    discipline = Discipline.objects.all().order_by('name', '-id').values()
    context = {'discipline': discipline}
    return render(request, 'disciplinelist.html', context)

def deletediscipline(request, pk):
    data = get_object_or_404(Discipline, id=pk)
    data.delete()
    return redirect('disciplinelist')


def thanks(request):
    return render(request, 'thanks.html',)

def createteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.get_timee = teacher.get_time()
            teacher.get_full_namee = teacher.get_full_name()
            teacher.get_job_title = teacher.get_job_title_display()
            teacher.get_za_stavka = teacher.get_za_stavkaa()
            teacher.get_stavka = teacher.get_stavkaa()
            teacher.zvaniiee = teacher.get_zvanie_display()

            form.save()
            return redirect('teacher')
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'createteacher.html', context)

def teacherlist(request):
    teacher = Teacher.objects.all
    context = {'teachers': teacher}
    return render(request, 'teacherlist.html', context)


def deleteteacher(request, pk):
    teach = get_object_or_404(Teacher, id=pk)
    teach.delete()
    return redirect('teacherlist')


# def updateteacher(request, pk):
#     data = get_object_or_404(Teacher, id=pk)
#     form = TeacherForm(instance=data)
#
#     if request.method == "POST":
#         form = TeacherForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             return redirect ('teacherlist')
#     context = {
#         "form":form
#     }
#     return render(request, 'createteacher.html', context)


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
    rows = Teacher.objects.all().values_list('get_full_namee', 'get_job_title', Sum('teacherr__group_id__lekcii_po_ucheb_planu'),
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
            form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = ConnectForm()
    context = {'form': form}
    return render(request, 'createconnects.html', context)

def connectlist(request):
    data = Connect.objects.all().order_by('-id')
    context = {'data': data}
    return render(request, 'connectlist.html', context)


def deleteconnect(request, pk):
    data = get_object_or_404(Connect, id=pk)
    data.delete()
    return redirect('connectlist')

def shtatnoe(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(vsego_uchebnyh_chasov=Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                                 za_vsego_uchebnyh_chasov=Sum('teacherr__group_id__za_vsego_uchebnyh_chasov')).order_by('-id')

        context = {'teachers': teacher}
        return render(request, 'shtatnoe.html', context)


def export_excel_shtatnoe(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Штатное расписание')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Ф.И.О преподователя', 'Занимаемая должность', 'Звание', 'Пед. стаж',
               'Штат. или совмест.', 'Штатные единицы/бюджет', 'Штатные единицы/контракт/очное',
               'Количество часов', 'Учебная нагрузка/контракт/очное',
               'Учебная нагрузка/контракт/заочное', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    rows = Teacher.objects.all().values_list('get_full_namee', 'get_job_title', 'zvaniiee', 'ped_staj',
                                             'shtat_sovmest', 'get_za_stavka', 'get_stavka', 'get_timee', Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                             Sum('teacherr__group_id__za_vsego_uchebnyh_chasov'),
                                             )


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)

    return response


class Search(ListView):
    paginated_by = 3
    template_name = 'teacher_list.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Teacher.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query)).annotate(total=Sum('teacherr__group_id__vsego_uchebnyh_chasov'))
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
