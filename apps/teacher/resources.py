from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DecimalWidget, IntegerWidget
from .models import Teacher, Doljnost


class TeacherResource(resources.ModelResource):
    get_full_name = fields.Field(
        column_name='Ф.И.О преподавателя',
        attribute='get_full_name',
        readonly=True)

    job_title = fields.Field(
        column_name='Должность',
        attribute='job_title',
        widget=ForeignKeyWidget(Doljnost, 'name'))

    zvanie = fields.Field(
        column_name='Звание',
        attribute='zvanie',
        readonly=True)

    ped_staj = fields.Field(
        column_name='Пед.стаж',
        attribute='ped_staj',
        readonly=True,
        widget=IntegerWidget())

    shtat_sovmest = fields.Field(
        column_name='Штат.или совмест.',
        attribute='shtat_sovmest',
        readonly=True)

    stavka_budget = fields.Field(
        column_name='Ставка для бюджета',
        attribute='stavka_budget',
        readonly=True,
        widget=DecimalWidget())

    stavka = fields.Field(
        column_name='Ставка',
        attribute='stavka',
        readonly=True,
        widget=DecimalWidget())

    vsego_stavka = fields.Field(
        column_name='Всего ставка',
        attribute='vsego_stavka',
        readonly=True,
        widget=DecimalWidget())

    get_time = fields.Field(
        column_name='Необходимые часы',
        attribute='get_time',
        readonly=True,
        widget=DecimalWidget()
    )

    get_time_budget = fields.Field(
        column_name='Необходимые часы бюджет',
        attribute='get_time_budget',
        readonly=True,
        widget=DecimalWidget()
    )

    get_title_stavka = fields.Field(
        column_name='Часы по должности',
        attribute='get_title_stavka',
        readonly=True,
        widget=DecimalWidget()
    )

    get_time_vsego = fields.Field(
        column_name='Всего часы',
        attribute='get_time_vsego',
        readonly=True,
        widget=DecimalWidget()
    )

    total_vsego_uchebnyh_chasov = fields.Field(
        column_name='Очное',
        attribute='total_vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())

    total_za_vsego_uchebnyh_chasov = fields.Field(
        column_name='Заочное',
        attribute='total_za_vsego_uchebnyh_chasov',
        readonly=True,
        widget=DecimalWidget())

    vsego = fields.Field(
        column_name='Всего',
        attribute='vsego',
        readonly=True,
        widget=DecimalWidget())



    class Meta:
        model = Teacher
        fields = ('get_full_name', 'job_title', 'get_title_stavka',
                    'zvanie', 'ped_staj', 'shtat_sovmest', 'stavka', 'stavka_budget', 'vsego_stavka', 'get_time',
                    'get_time_budget', 'get_time_vsego',
                    'total_vsego_uchebnyh_chasov', 'total_za_vsego_uchebnyh_chasov', 'vsego')
        export_order = fields