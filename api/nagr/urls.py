from django.urls import path
from . import views

urlpatterns = [
    path('thanks/', views.thanks, name='thanks'),
    path('vedomost/', views.vedomost, name='vedomost'),
    
    path('createconnects', views.createconnects, name='createconnects'),
    path('connectlist/', views.connectlist, name='connectlist'),
    path('deleteconnect/<int:pk>', views.deleteconnect, name='deleteconnect'),
    
    path('export_excel/<int:pk>', views.export_excel, name='export_excel'),
    path('export_excel_vedomost/', views.export_excel_vedomost, name='export_excel_vedomost'),
]