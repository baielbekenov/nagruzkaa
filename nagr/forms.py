from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from nagr.models import Groupp, Discipline, Teacher, Connect


class GrouppForm(ModelForm):

    class Meta:
        model = Groupp
        fields = ('name', 'zaochnoe', 'for_discipline', 'kol_stud_budget', 'kol_stud_contract', 'semester', 'sovmest',
                  'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku',
                  'praktZan_po_ucheb_planu', 'praktZan_zachityvaetsa_v_nagruzku',
                  'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku', 'rukovodstvo_kafedroi', 'rukovodstvo_dekanatom'
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Добавить'))


class DisciplineForm(ModelForm):

    class Meta:
        model = Discipline
        fields = '__all__'



class TeacherForm(ModelForm):

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'is_budget', 'job_title', 'zvanie',
                  'ped_staj', 'shtat_sovmest', 'stavka')


class ConnectForm(ModelForm):

    class Meta:
        model = Connect
        fields = '__all__'

