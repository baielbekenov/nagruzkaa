from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DecimalWidget, IntegerWidget
from apps.group.models import Groupp


class GrouppResource(resources.ModelResource):
    discipline_name = fields.Field(
        column_name='Дисциплины',
        attribute='discipline_name',
        readonly=True)

    amount_of_credit = fields.Field(
        column_name='Количество кредитов',
        attribute='amount_of_credit',
        readonly=True,
        widget=IntegerWidget())

    name = fields.Field(
        column_name='Название группы',
        attribute='name',
        readonly=True)

    kol_stud_budget = fields.Field(
        column_name='Кол. студ.бюджет',
        attribute='kol_stud_budget',
        readonly=True,
        widget=IntegerWidget())

    kol_stud_contract = fields.Field(
        column_name='Кол. студ.контракт',
        attribute='kol_stud_contract',
        readonly=True,
        widget=IntegerWidget())

    obshee_kol_stud = fields.Field(
        column_name='Общее кол.студентов',
        attribute='obshee_kol_stud',
        readonly=True,
        widget=DecimalWidget())

    semester = fields.Field(
        column_name='Семестер',
        attribute='semester',
        readonly=True,
        widget=IntegerWidget())

    lekcii_po_ucheb_planu = fields.Field(
        column_name='Лекции/ По учебному плану',
        attribute='lekcii_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    lekcii_zachityvaetsa_v_nagruzku = fields.Field(
        column_name='Лекции/ Зачитывается в нагрузку кафедры (ч.)',
        attribute='lekcii_zachityvaetsa_v_nagruzku',
        readonly=True,
        widget=DecimalWidget())

    praktZan_po_ucheb_planu = fields.Field(
        column_name='Практ.зан/ По учебному плану',
        attribute='praktZan_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    praktZan_zachityvaetsa_v_nagruzku = fields.Field(
        column_name='Практ.зан/ Зачитывается в нагрузку кафедры (ч.)',
        attribute='praktZan_zachityvaetsa_v_nagruzku',
        readonly=True,
        widget=DecimalWidget())

    labRab_po_ucheb_planu = fields.Field(
        column_name='Лаб.раб/ По учебному плану',
        attribute='labRab_po_ucheb_planu',
        readonly=True,
        widget=DecimalWidget())

    labRab_zachityvaetsa_v_nagruzku = fields.Field(
        column_name='Лаб.раб/ Зачитывается в нагрузку кафедры (ч.)',
        attribute='labRab_zachityvaetsa_v_nagruzku',
        readonly=True,
        widget=DecimalWidget())

    rukovod_KRIKP = fields.Field(
        column_name='Руковод.КРиКП',
        attribute='rukovod_KRIKP',
        readonly=True,
        widget=DecimalWidget())

    recenzirov_KR = fields.Field(
        column_name='Рецениров_КР',
        attribute='recenzirov_KR',
        readonly=True,
        widget=DecimalWidget())

    priem_SRS = fields.Field(
        column_name='Прием СРС',
        attribute='priem_SRS',
        readonly=True,
        widget=DecimalWidget())

    praktika_uchebnay = fields.Field(
        column_name='Практика/Учебная',
        attribute='praktika_uchebnay',
        readonly=True,
        widget=DecimalWidget())

    praktika_proizvod = fields.Field(
        column_name='Практика/Производ',
        attribute='praktika_proizvod',
        readonly=True,
        widget=DecimalWidget())

    praktika_predkval = fields.Field(
        column_name='Практика/Предквал',
        attribute='praktika_predkval',
        readonly=True,
        widget=DecimalWidget())

    praktika_pedagog = fields.Field(
        column_name='Практика/Педагогическая',
        attribute='praktika_pedagog',
        readonly=True,
        widget=DecimalWidget())

    praktika_nauchno = fields.Field(
        column_name='Практика/Научно-исследовательская',
        attribute='praktika_nauchno',
        readonly=True,
        widget=DecimalWidget())

    kontrol_tekuchiy1 = fields.Field(
        column_name='Контроль/текущий (1 контр.точка)',
        attribute='kontrol_tekuchiy1',
        readonly=True,
        widget=DecimalWidget())

    kontrol_tekuchiy2 = fields.Field(
        column_name='Контроль/текущий (2 контр.точка)',
        attribute='kontrol_tekuchiy2',
        readonly=True,
        widget=DecimalWidget())

    kontrol_tekuchiy3 = fields.Field(
        column_name='Контроль/текущий (3 контр.точка)',
        attribute='kontrol_tekuchiy3',
        readonly=True,
        widget=DecimalWidget())

    kontrol_itogovyi = fields.Field(
        column_name='Контроль/итоговый (экзамен)',
        attribute='kontrol_itogovyi',
        readonly=True,
        widget=DecimalWidget())

    zachita_rukovod_VKR = fields.Field(
        column_name='Защита вып. квал. работы/ руководство ВКР',
        attribute='zachita_rukovod_VKR',
        readonly=True,
        widget=DecimalWidget())

    zachita_konsult = fields.Field(
        column_name='Защита вып. квал. работы/ консульт. по разделам',
        attribute='zachita_konsult',
        readonly=True,
        widget=DecimalWidget())

    zachita_recencirovanie = fields.Field(
        column_name='Защита вып. квал. работы/ рецензирование',
        attribute='zachita_recencirovanie',
        readonly=True,
        widget=DecimalWidget())

    zachita_uchastie_v_GAK = fields.Field(
        column_name='Защита вып. квал. работы/ участие в ГАК',
        attribute='zachita_uchastie_v_GAK',
        readonly=True,
        widget=DecimalWidget())

    normokontr = fields.Field(
        column_name='Нормоконтр',
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

    online = fields.Field(
        column_name='Онлайн',
        attribute='online',
        readonly=True,
        widget=DecimalWidget())

    offline = fields.Field(
        column_name='Офлайн',
        attribute='offline',
        readonly=True,
        widget=DecimalWidget())

    academ_sov = fields.Field(
        column_name='Академ. сов.',
        attribute='academ_sov',
        readonly=True,
        widget=DecimalWidget())

    rukovodstvo_kafedroi = fields.Field(
        column_name='Руководство кафедрой',
        attribute='rukovodstvo_kafedroi',
        readonly=True,
        widget=DecimalWidget())

    rukovodstvo_dekanatom = fields.Field(
        column_name='Руководство деканатом',
        attribute='rukovodstvo_dekanatom',
        readonly=True,
        widget=DecimalWidget())

    prochie = fields.Field(
        column_name='Прочие',
        attribute='prochie',
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
        model = Groupp
        fields = ('discipline_name', 'amount_of_credit', 'name', 'vsego_uchebnyh_chasov', 'kol_stud_budget', 'kol_stud_contract', 'obshee_kol_stud', 'semester',
                    'lekcii_po_ucheb_planu', 'lekcii_zachityvaetsa_v_nagruzku', 'praktZan_po_ucheb_planu',
                    'praktZan_zachityvaetsa_v_nagruzku', 'labRab_po_ucheb_planu', 'labRab_zachityvaetsa_v_nagruzku',
                    'rukovod_KRIKP', 'recenzirov_KR', 'priem_SRS', 'praktika_uchebnay',
                    'praktika_proizvod', 'praktika_predkval', 'praktika_pedagog', 'praktika_nauchno',
                    'kontrol_tekuchiy1', 'kontrol_tekuchiy2', 'kontrol_tekuchiy3', 'kontrol_itogovyi',
                    'zachita_rukovod_VKR', 'zachita_konsult', 'zachita_recencirovanie', 'zachita_uchastie_v_GAK',
                    'normokontr', 'magistratura', 'aspirantura_doctorontura', 'online', 'offline', 'academ_sov',
                    'rukovodstvo_kafedroi', 'rukovodstvo_dekanatom', 'prochie', 'vsego_uchebnyh_chasov', 'za_vsego_uchebnyh_chasov')
        export_order = fields