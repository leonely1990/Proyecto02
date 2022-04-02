from dataclasses import fields
import imp
from pyexpat import model
from django.forms.models import ModelForm
from .models import Equipo

class EquipoForm(ModelForm):
    
    class Meta:
        model = Equipo
        fields = '__all__'