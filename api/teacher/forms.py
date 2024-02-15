from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from apps.teacher.models import Teacher


class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'