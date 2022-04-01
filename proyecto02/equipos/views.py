from xxlimited import foo
from django.shortcuts import render, redirect
from .models import Equipo

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