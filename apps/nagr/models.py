from django.db import models
from apps.group.models import Groupp 
from apps.teacher.models import Teacher
from django.db.models import Sum


# Create your models here.


class Nagruzka(models.Model):
    name = models.CharField(max_length=123, verbose_name='Название', blank=True, null=True)
    group_id = models.ForeignKey(Groupp, on_delete=models.CASCADE, verbose_name='Группа')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacherr', verbose_name='Преподователь')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Распределение нагрузки'
        verbose_name_plural = 'Распределение нагрузки'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.group_id.name}"
        super().save(*args, **kwargs)
        self.update_teacher_summary()

    def update_teacher_summary(self):
        teacher = self.teacher
        summary, created = TeacherSummary.objects.get_or_create(teacher=teacher)
        summary.save()

    def discipline_name(self):
        return self.group_id.discipline_name

    discipline_name.short_description = 'Дисциплины'

    def lekcii_po_ucheb_planu(self):
        return self.group_id.lekcii_po_ucheb_planu
    lekcii_po_ucheb_planu.short_description = 'Лекции по учебному плану'

    def praktZan_po_ucheb_planu(self):
        return self.group_id.praktZan_po_ucheb_planu
    praktZan_po_ucheb_planu.short_description = 'Практические занятия по учебному плану'

    def labRab_po_ucheb_planu(self):
        return self.group_id.labRab_po_ucheb_planu
    labRab_po_ucheb_planu.short_description = 'Лабораторные работы по учебному плану'

    def rukovod_KRIKP(self):
        return self.group_id.rukovod_KRIKP
    rukovod_KRIKP.short_description = 'Руководство КРиКП'

    def recenzirov_KR(self):
        return self.group_id.recenzirov_KR
    recenzirov_KR.short_description = 'Рецензирование КР'

    def priem_SRS(self):
        return round(self.group_id.priem_SRS, 1)
    priem_SRS.short_description = 'Прием СРС'

    def praktika_uchebnay(self):
        return self.group_id.praktika_uchebnay
    praktika_uchebnay.short_description = 'Учебная практика'

    def praktika_proizvod(self):
        return self.group_id.praktika_proizvod
    praktika_proizvod.short_description = 'Производственная практика'

    def praktika_predkval(self):
        return self.group_id.praktika_predkval
    praktika_predkval.short_description = 'Предквалификационная практика'

    def praktika_pedagog(self):
        return self.group_id.praktika_pedagog
    praktika_pedagog.short_description = 'Педагогическая практика'

    def praktika_nauchno(self):
        return self.group_id.praktika_nauchno
    praktika_nauchno.short_description = 'Научно-исследовательская практика'

    def kontrol_itogovyi(self):
        return round(self.group_id.kontrol_itogovyi, 1)
    kontrol_itogovyi.short_description = 'Итоговый контроль (экзамен)'

    def zachita_rukovod_VKR(self):
        return self.group_id.zachita_rukovod_VKR
    zachita_rukovod_VKR.short_description = 'Руководство ВКР'

    def zachita_konsult(self):
        return self.group_id.zachita_konsult
    zachita_konsult.short_description = 'Консультирование по разделам'

    def zachita_recencirovanie(self):
        return self.group_id.zachita_recencirovanie
    zachita_recencirovanie.short_description = 'Рецензирование'

    def zachita_uchastie_v_GAK(self):
        return self.group_id.zachita_uchastie_v_GAK
    zachita_uchastie_v_GAK.short_description = 'Участие в ГАК'

    def normokontr(self):
        return self.group_id.normokontr
    normokontr.short_description = 'Нормоконтроль'

    def magistratura(self):
        return self.group_id.magistratura
    magistratura.short_description = 'Магистратура'

    def aspirantura_doctorontura(self):
        return self.group_id.aspirantura_doctorontura
    aspirantura_doctorontura.short_description = 'Аспирантура, докторантура'

    def academ_sov(self):
        return self.group_id.academ_sov
    academ_sov.short_description = 'Академический совет'

    def rukovodstvo_kafedroi(self):
        return self.group_id.rukovodstvo_kafedroi
    rukovodstvo_kafedroi.short_description = 'Руководство кафедрой'

    def vsego_uchebnyh_chasov(self):
        return round(self.group_id.vsego_uchebnyh_chasov, 1)
    vsego_uchebnyh_chasov.short_description = 'Всего учебных часов'

    def za_vsego_uchebnyh_chasov(self):
        return round(self.group_id.za_vsego_uchebnyh_chasov, 1)
    za_vsego_uchebnyh_chasov.short_description = 'Всего учебных часов заочно'


class TeacherSummary(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, primary_key=True,
                                   verbose_name='Преподователь', related_name='summary')

    class Meta:
        managed = True
        verbose_name = 'Сводная ведомость'
        verbose_name_plural = 'Сводные ведомости'

    @property
    def total_lekcii_po_ucheb_planu(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__lekcii_po_ucheb_planu'))[
            'group_id__lekcii_po_ucheb_planu__sum'] or 0

    @property
    def total_praktZan_po_ucheb_planu(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktZan_po_ucheb_planu'))[
            'group_id__praktZan_po_ucheb_planu__sum'] or 0

    @property
    def total_labRab_po_ucheb_planu(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__labRab_po_ucheb_planu'))[
            'group_id__labRab_po_ucheb_planu__sum'] or 0

    @property
    def total_rukovod_KRIKP(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__rukovod_KRIKP'))['group_id__rukovod_KRIKP__sum'] or 0

    @property
    def total_recenzirov_KR(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__recenzirov_KR'))['group_id__recenzirov_KR__sum'] or 0

    @property
    def total_priem_SRS(self):
        return round(self.teacher.teacherr.aggregate(Sum('group_id__priem_SRS'))['group_id__priem_SRS__sum'], 1) or 0.0

    @property
    def total_praktika_uchebnay(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktika_uchebnay'))[
            'group_id__praktika_uchebnay__sum'] or 0

    @property
    def total_praktika_proizvod(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktika_proizvod'))[
            'group_id__praktika_proizvod__sum'] or 0

    @property
    def total_praktika_predkval(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktika_predkval'))[
            'group_id__praktika_predkval__sum'] or 0

    @property
    def total_praktika_pedagog(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktika_pedagog'))[
            'group_id__praktika_pedagog__sum'] or 0

    @property
    def total_praktika_nauchno(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__praktika_nauchno'))[
            'group_id__praktika_nauchno__sum'] or 0

    @property
    def total_kontrol_itogovyi(self):
        return round(self.teacher.teacherr.aggregate(Sum('group_id__kontrol_itogovyi'))[
            'group_id__kontrol_itogovyi__sum'], 1) or 0.0

    @property
    def total_zachita_rukovod_VKR(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__zachita_rukovod_VKR'))[
            'group_id__zachita_rukovod_VKR__sum'] or 0.0

    @property
    def total_zachita_konsult(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__zachita_konsult'))[
            'group_id__zachita_konsult__sum'] or 0.0

    @property
    def total_zachita_recencirovanie(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__zachita_recencirovanie'))[
            'group_id__zachita_recencirovanie__sum'] or 0.0

    @property
    def total_zachita_uchastie_v_GAK(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__zachita_uchastie_v_GAK'))[
            'group_id__zachita_uchastie_v_GAK__sum'] or 0.0

    @property
    def total_normokontr(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__normokontr'))['group_id__normokontr__sum'] or 0.0

    @property
    def total_magistratura(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__magistratura'))['group_id__magistratura__sum'] or 0.0

    @property
    def total_aspirantura_doctorontura(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__aspirantura_doctorontura'))[
            'group_id__aspirantura_doctorontura__sum'] or 0.0

    @property
    def total_academ_sov(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__academ_sov'))['group_id__academ_sov__sum'] or 0.0

    @property
    def total_rukovodstvo_kafedroi(self):
        return self.teacher.teacherr.aggregate(Sum('group_id__rukovodstvo_kafedroi'))[
            'group_id__rukovodstvo_kafedroi__sum'] or 0.0
    @property
    def total_vsego_uchebnyh_chasov(self):
        return round(self.teacher.teacherr.aggregate(Sum('group_id__vsego_uchebnyh_chasov'))[
            'group_id__vsego_uchebnyh_chasov__sum'], 1) or 0.0

    @property
    def total_za_vsego_uchebnyh_chasov(self):
        return round(self.teacher.teacherr.aggregate(Sum('group_id__za_vsego_uchebnyh_chasov'))[
            'group_id__za_vsego_uchebnyh_chasov__sum'], 1) or 0.0





