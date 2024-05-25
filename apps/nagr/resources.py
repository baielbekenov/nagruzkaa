from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DecimalWidget
from apps.nagr.models import TeacherSummary


class NagruzkaResource(resources.ModelResource):
    teacher = fields.Field(
        column_name='Преподаватель',
        attribute='teacher',
        readonly=True)

    name = fields.Field(
        column_name='Название',
        attribute='name',
        readonly=True)

    semester_type = fields.Field(
        column_name='Тип семестра',
        attribute='semester_type',
        readonly=True)

    discipline_name = fields.Field(
        column_name='Дисциплины',
        attribute='discipline_name',
        readonly=True)

    lekcii_po_ucheb_planu = fields.Field(
        column_name='Лекции',
        attribute='lekcii_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    praktZan_po_ucheb_planu = fields.Field(
        column_name='Практические занятия',
        attribute='praktZan_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    labRab_po_ucheb_planu = fields.Field(
        column_name='Лабораторные работы',
        attribute='labRab_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    rukovod_KRIKP = fields.Field(
        column_name='Руководство КРИКП',
        attribute='rukovod_KRIKP',
        readonly=True,
        widget=DecimalWidget())

    recenzirov_KR = fields.Field(
        column_name='Рецензирование КР',
        attribute='recenzirov_KR',
        readonly=True,
        widget=DecimalWidget())

    priem_SRS = fields.Field(
        column_name='Прием СРС',
        attribute='priem_SRS',
        readonly=True,
        widget=DecimalWidget())

    praktika_uchebnay = fields.Field(
        column_name='Учебная практика',
        attribute='praktika_uchebnay',
        readonly=True,
        widget=DecimalWidget())

    praktika_proizvod = fields.Field(
        column_name='Производственная практика',
        attribute='praktika_proizvod',
        readonly=True,
        widget=DecimalWidget())

    praktika_predkval = fields.Field(
        column_name='Предквалификационная практика',
        attribute='praktika_predkval',
        readonly=True,
        widget=DecimalWidget())

    praktika_pedagog = fields.Field(
        column_name='Педагогическая практика',
        attribute='praktika_pedagog',
        readonly=True,
        widget=DecimalWidget())

    praktika_nauchno = fields.Field(
        column_name='Научно-исследовательская практика',
        attribute='praktika_nauchno',
        readonly=True,
        widget=DecimalWidget())

    kontrol_itogovyi = fields.Field(
        column_name='Итоговый контроль (экзамен)',
        attribute='kontrol_itogovyi',
        readonly=True,
        widget=DecimalWidget())

    zachita_rukovod_VKR = fields.Field(
        column_name='Руководство ВКР',
        attribute='zachita_rukovod_VKR',
        readonly=True,
        widget=DecimalWidget())

    zachita_konsult = fields.Field(
        column_name='Консультирование по разделам',
        attribute='zachita_konsult',
        readonly=True,
        widget=DecimalWidget())

    zachita_recencirovanie = fields.Field(
        column_name='Рецензирование',
        attribute='zachita_recencirovanie',
        readonly=True,
        widget=DecimalWidget())

    zachita_uchastie_v_GAK = fields.Field(
        column_name='Участие в ГАК',
        attribute='zachita_uchastie_v_GAK',
        readonly=True,
        widget=DecimalWidget())

    normokontr = fields.Field(
        column_name='Нормоконтроль',
        attribute='normokontr',
        readonly=True,
        widget=DecimalWidget())

    magistratura = fields.Field(
        column_name='Магистратура',
        attribute='magistratura',
        readonly=True,
        widget=DecimalWidget())

    aspirantura_doctorontura = fields.Field(
        column_name='Аспирантура, докторантура',
        attribute='aspirantura_doctorontura',
        readonly=True,
        widget=DecimalWidget())

    academ_sov = fields.Field(
        column_name='Академический совет',
        attribute='academ_sov',
        readonly=True,
        widget=DecimalWidget())

    rukovodstvo_kafedroi = fields.Field(
        column_name='Руководство кафедрой',
        attribute='rukovodstvo_kafedroi',
        readonly=True,
        widget=DecimalWidget())

    vsego_uchebnyh_chasov = fields.Field(
        column_name='Всего учебных часов',
        attribute='vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())

    za_vsego_uchebnyh_chasov = fields.Field(
        column_name='Всего учебных часов заочно',
        attribute='za_vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())

    class Meta:
        model = TeacherSummary
        fields = ('teacher', 'name', 'semester_type', 'discipline_name', 'lekcii_po_ucheb_planu', 'praktZan_po_ucheb_planu',
                  'labRab_po_ucheb_planu', 'rukovod_KRIKP', 'recenzirov_KR',
                  'priem_SRS', 'praktika_uchebnay', 'praktika_proizvod',
                  'praktika_predkval', 'praktika_pedagog', 'praktika_nauchno',
                  'kontrol_itogovyi', 'zachita_rukovod_VKR', 'zachita_konsult',
                  'zachita_recencirovanie', 'zachita_uchastie_v_GAK', 'normokontr',
                  'magistratura', 'aspirantura_doctorontura', 'academ_sov',
                  'rukovodstvo_kafedroi', 'vsego_uchebnyh_chasov', 'za_vsego_uchebnyh_chasov')
        export_order = fields


class TeacherSummaryResource(resources.ModelResource):
    teacher = fields.Field(
        column_name='Преподаватель',
        attribute='teacher',
        readonly=True)

    total_lekcii_po_ucheb_planu = fields.Field(
        column_name='Лекции',
        attribute='total_lekcii_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    total_praktZan_po_ucheb_planu = fields.Field(
        column_name='Практические занятия',
        attribute='total_praktZan_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    total_labRab_po_ucheb_planu = fields.Field(
        column_name='Лабораторные работы',
        attribute='total_labRab_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    total_rukovod_KRIKP = fields.Field(
        column_name='Руководство КРИКП',
        attribute='total_rukovod_KRIKP',
        readonly=True,
        widget=DecimalWidget())

    total_recenzirov_KR = fields.Field(
        column_name='Рецензирование КР',
        attribute='total_recenzirov_KR',
        readonly=True,
        widget=DecimalWidget())

    total_priem_SRS = fields.Field(
        column_name='Прием СРС',
        attribute='total_priem_SRS',
        readonly=True,
        widget=DecimalWidget())

    total_praktika_uchebnay = fields.Field(
        column_name='Учебная практика',
        attribute='total_praktika_uchebnay',
        readonly=True,
        widget=DecimalWidget())

    total_praktika_proizvod = fields.Field(
        column_name='Производственная практика',
        attribute='total_praktika_proizvod',
        readonly=True,
        widget=DecimalWidget())

    total_praktika_predkval = fields.Field(
        column_name='Предквалификационная практика',
        attribute='total_praktika_predkval',
        readonly=True,
        widget=DecimalWidget())

    total_praktika_pedagog = fields.Field(
        column_name='Педагогическая практика',
        attribute='total_praktika_pedagog',
        readonly=True,
        widget=DecimalWidget())

    total_praktika_nauchno = fields.Field(
        column_name='Научно-исследовательская практика',
        attribute='total_praktika_nauchno',
        readonly=True,
        widget=DecimalWidget())

    total_kontrol_itogovyi = fields.Field(
        column_name='Итоговый контроль (экзамен)',
        attribute='total_kontrol_itogovyi',
        readonly=True,
        widget=DecimalWidget())

    total_zachita_rukovod_VKR = fields.Field(
        column_name='Руководство ВКР',
        attribute='total_zachita_rukovod_VKR',
        readonly=True,
        widget=DecimalWidget())

    total_zachita_konsult = fields.Field(
        column_name='Консультирование по разделам',
        attribute='total_zachita_konsult',
        readonly=True,
        widget=DecimalWidget())

    total_zachita_recencirovanie = fields.Field(
        column_name='Рецензирование',
        attribute='total_zachita_recencirovanie',
        readonly=True,
        widget=DecimalWidget())

    total_zachita_uchastie_v_GAK = fields.Field(
        column_name='Участие в ГАК',
        attribute='total_zachita_uchastie_v_GAK',
        readonly=True,
        widget=DecimalWidget())

    total_normokontr = fields.Field(
        column_name='Нормоконтроль',
        attribute='total_normokontr',
        readonly=True,
        widget=DecimalWidget())

    total_magistratura = fields.Field(
        column_name='Магистратура',
        attribute='total_magistratura',
        readonly=True,
        widget=DecimalWidget())

    total_aspirantura_doctorontura = fields.Field(
        column_name='Аспирантура, докторантура',
        attribute='total_aspirantura_doctorontura',
        readonly=True,
        widget=DecimalWidget())

    total_academ_sov = fields.Field(
        column_name='Академический совет',
        attribute='total_academ_sov',
        readonly=True,
        widget=DecimalWidget())

    total_rukovodstvo_kafedroi = fields.Field(
        column_name='Руководство кафедрой',
        attribute='total_rukovodstvo_kafedroi',
        readonly=True,
        widget=DecimalWidget())

    total_vsego_uchebnyh_chasov = fields.Field(
        column_name='Всего учебных часов',
        attribute='total_vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())

    total_za_vsego_uchebnyh_chasov = fields.Field(
        column_name='Всего учебных часов заочно',
        attribute='total_za_vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())
    
    class Meta:
        model = TeacherSummary
        fields = ('teacher', 'total_lekcii_po_ucheb_planu',  'total_praktZan_po_ucheb_planu',
                  'total_labRab_po_ucheb_planu', 'total_rukovod_KRIKP', 'total_recenzirov_KR',
                  'total_priem_SRS', 'total_praktika_uchebnay', 'total_praktika_proizvod',
                  'total_praktika_predkval', 'total_praktika_pedagog', 'total_praktika_nauchno',
                  'total_kontrol_itogovyi', 'total_zachita_rukovod_VKR', 'total_zachita_konsult',
                  'total_zachita_recencirovanie', 'total_zachita_uchastie_v_GAK', 'total_normokontr',
                  'total_magistratura', 'total_aspirantura_doctorontura', 'total_academ_sov',
                  'total_rukovodstvo_kafedroi', 'total_vsego_uchebnyh_chasov', 'total_za_vsego_uchebnyh_chasov')
        export_order = fields