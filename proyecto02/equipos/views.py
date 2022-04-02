from xxlimited import foo
from django.shortcuts import render, redirect
from .models import Equipo
from .form import *

# Create your views here.

def equipos(request):
    
    if request.method == 'GET':
        for nose in request.GET:
            print(nose)
    
    equipos = Equipo.objects.order_by('id')
    
    contexto = {'equipos': equipos}    
    
    return render(request, 'equipos.html', contexto)


def registrarEquipo(request):    
    
    if request.method == 'POST':
        pass
        
    
    return redirect(to='Equipos:inicio')

def formula(request):
    
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Equipos:inicio')
    
    formulario = EquipoForm().as_p()
    
    contexto = {'formulario':formulario}
    
    return render(request, 'formIndex.html', contexto)