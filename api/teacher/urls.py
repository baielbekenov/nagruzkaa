from django.urls import path
from . import views


urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('group_teacher/<int:pk>', views.group_teacher, name='group_teacher'),
    path('createteacher/', views.createteacher, name='createteacher'),
    path('teacherlist/', views.teacherlist, name='teacherlist'),
    path('deleteteacher/<int:pk>/', views.deleteteacher, name='deleteteacher'),
    path('updateteacher/<int:pk>/', views.updateteacher, name='updateteacher'),
    path('shtatnoe/', views.shtatnoe, name='shtatnoe'),
]