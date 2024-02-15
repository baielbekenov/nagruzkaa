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
            return redirect('/')
    else:
        form = GrouppForm()
    content = {'form': form}
    return render(request, 'create.html', content)


def deletegroup(request, pk):
    group = get_object_or_404(Groupp, id=pk)
    group.delete()
    return redirect('/')


def showgroup(request):
    group = Groupp.objects.all()
    context = {'groups': group}
    return render(request, 'showgroup.html', context)