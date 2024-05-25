from django.contrib.admin import SimpleListFilter


class SemesterTypeFilter(SimpleListFilter):
    title = 'Тип семестра'
    parameter_name = 'semester_type'

    def lookups(self, request, model_admin):
        return (
            ('spring', 'Весенний семестер'),
            ('autumn', 'Осенний семестер'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'spring':
            return queryset.filter(group_id__semester__in=[i for i in range(1, 11) if i % 2 == 0])
        if self.value() == 'autumn':
            return queryset.filter(group_id__semester__in=[i for i in range(1, 11) if i % 2 != 0])
        return queryset
