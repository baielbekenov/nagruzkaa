from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from nagr.models import Groupp, Discipline, Teacher, Connect, Group


class GrouppForm(ModelForm):

    class Meta:
        model = Groupp
        fields = ('name', 'for_discipline', 'kol_stud_budget', 'kol_stud_contract', 'semester',
                  'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku',
                  'praktZan_po_ucheb_planu', 'praktZan_zachityvaetsa_v_nagruzku',
                  'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить'))


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ('name_id', 'zaochnoe', 'rukovodstvo_kafedroi', 'rukovodstvo_dekanatom')


class DisciplineForm(ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'



class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = '__all__'


class ConnectForm(ModelForm):

    class Meta:
        model = Connect
        fields = '__all__'

