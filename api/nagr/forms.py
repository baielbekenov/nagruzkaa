from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from apps.nagr.models import Nagruzka


class NagruzkaForm(ModelForm):

    class Meta:
        model = Nagruzka
        fields = '__all__'