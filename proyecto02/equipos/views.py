from django.shortcuts import render

# Create your views here.

def equipos(request):
    return render(request, 'equipos.html')