from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from apps.discipline.models import Discipline


class DisciplineForm(ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'