from django.urls import path

from . import views

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('create/', views.create, name='create'),
    path('deletegroup/<int:pk>/', views.deletegroup, name='deletegroup'),
    path('group_teacher/<int:pk>', views.group_teacher, name='group_teacher'),
    path('creatediscipline/', views.creatediscipline, name='creatediscipline'),
    path('disciplinelist/', views.disciplinelist, name='disciplinelist'),
    path('deletediscipline/<int:pk>/', views.deletediscipline, name='deletediscipline'),
    path('createteacher/', views.createteacher, name='createteacher'),
    path('deleteteacher/<int:pk>/', views.deleteteacher, name='deleteteacher'),
    path('teacherlist/', views.teacherlist, name='teacherlist'),
    path('updateteacher/<int:pk>/', views.updateteacher, name='updateteacher'),
    path('createconnects', views.createconnects, name='createconnects'),
    path('connectlist/', views.connectlist, name='connectlist'),
    path('deleteconnect/<int:pk>', views.deleteconnect, name='deleteconnect'),
    path('shtatnoe/', views.shtatnoe, name='shtatnoe'),
    path('thanks/', views.thanks, name='thanks'),
    path('vedomost/', views.vedomost, name='vedomost'),
    path('export_excel/<int:pk>', views.export_excel, name='export_excel'),
    path('export_excel_vedomost/', views.export_excel_vedomost, name='export_excel_vedomost'),
    path('showgroup/', views.showgroup, name='showgroup'),
    path('thanks/', views.thanks, name='thanks'),
]