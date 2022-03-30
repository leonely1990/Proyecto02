import imp
from django.shortcuts import render
from .models import Equipo

# Create your views here.

def equipos(request):
    
    equipos = Equipo.objects.order_by('id')
    
    contexto = {'equipos': equipos}    
    
    return render(request, 'equipos.html', contexto)


def registrarEquipo(request):
    
    
    return render(request, )