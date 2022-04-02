from django.urls import path
from . import views

app_name = 'Equipos'

urlpatterns = [
    path('', views.equipos, name='inicio'),
]
