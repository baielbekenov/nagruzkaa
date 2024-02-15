from django.urls import path
from . import views

urlpatterns = [
    path('creatediscipline/', views.creatediscipline, name='creatediscipline'),
    path('disciplinelist/', views.disciplinelist, name='disciplinelist'),
    path('deletediscipline/<int:pk>/', views.deletediscipline, name='deletediscipline'),
]