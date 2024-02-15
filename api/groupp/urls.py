from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('deletegroup/<int:pk>/', views.deletegroup, name='deletegroup'),
    path('showgroup/', views.showgroup, name='showgroup'),
]