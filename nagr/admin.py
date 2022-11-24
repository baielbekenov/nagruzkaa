from django.contrib import admin

from nagr.models import Discipline, Groupp, Teacher, Connect, Group

# Register your models here.

admin.site.register(Discipline)
admin.site.register(Groupp)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Connect)