from django.urls import path
from . import views

app_name = 'Equipos'

urlpatterns = [
    path('', views.equipos, name='inicio'),
    path('prubea/', views.registrarEquipo, name='registro'),
    path('formulario/', views.formula, name='formulario'),
]
