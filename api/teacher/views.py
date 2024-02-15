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


def teacher(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(total=Sum('teacherr__group_id__vsego_uchebnyh_chasov')).order_by('-id')


        context = {'teachers': teacher}
        return render(request, 'teacher.html', context)
    return HttpResponse('Error')


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


def createteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            # if teacher.doljnost == 1:
            #     teacher.stavka = 750

            return HttpResponseRedirect('/thanks/')
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


def updateteacher(request, pk):
    data = get_object_or_404(Teacher, id=pk)
    form = TeacherForm(instance=data)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect ('teacherlist')
    context = {
        "form":form
    }
    return render(request, 'createteacher.html', context)


def shtatnoe(request):
    if request.method == 'GET':
        teacher = Teacher.objects.all().annotate(vsego_uchebnyh_chasov=Sum('teacherr__group_id__vsego_uchebnyh_chasov'),
                                                 za_vsego_uchebnyh_chasov=Sum('teacherr__group_id__za_vsego_uchebnyh_chasov')).order_by('-id')

        context = {'teachers': teacher}
        return render(request, 'shtatnoe.html', context)