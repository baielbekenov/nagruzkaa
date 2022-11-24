from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('create/', views.create, name='create'),
    path('create1/', views.create1, name='create1'),
    path('group_teacher/<int:pk>', views.group_teacher, name='group_teacher'),
    path('creatediscipline/', views.creatediscipline, name='creatediscipline'),
    path('createteacher/', views.createteacher, name='createteacher'),
    path('createconnects', views.createconnects, name='createconnects'),
    path('shtatnoe/', views.shtatnoe, name='shtatnoe'),
    path('thanks/', views.thanks, name='thanks'),
    path('vedomost/', views.vedomost, name='vedomost'),
    path('export_excel/<int:pk>', views.export_excel, name='export_excel'),
    path('export_excel_vedomost/', views.export_excel_vedomost, name='export_excel_vedomost'),
    path('showgroupp/', views.showgroupp, name='showgroupp'),
    path('thanks/', views.thanks, name='thanks'),
]