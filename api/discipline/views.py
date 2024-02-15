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
    return redirect('/')