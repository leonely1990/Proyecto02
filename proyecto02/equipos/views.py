from xxlimited import foo
from django.shortcuts import render, redirect
from .models import Equipo
from .form import *

# Create your views here.

def equipos(request):
    
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Equipos:inicio')
    
    
    equipos = Equipo.objects.order_by('id')
    formulario = EquipoForm().as_p()
    
    contexto = {
        'equipos': equipos,
        'formulario': formulario,
    }    
    
    return render(request, 'equipos.html', contexto)