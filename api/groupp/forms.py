from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from apps.group.models import Groupp


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