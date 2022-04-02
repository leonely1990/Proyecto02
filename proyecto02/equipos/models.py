from django.db import models

# Create your models here.

class Equipo(models.Model):
    
    marca = models.CharField(
        verbose_name='Marca',
        max_length=255,
    )
    
    modelo = models.CharField(
        verbose_name='Modelo',
        max_length=255
    )
    
    n_bien_nacional = models.CharField(
        verbose_name='Numero de Bien',
        max_length=255,
        unique=True
    )
    
    PROCESADORES = (
        ('i3', 'I3'),
        ('i5', 'I5'),
        ('i7', 'I7')
    )
    
    procesador = models.CharField(
        verbose_name='Procesador',
        max_length=2,
        choices=PROCESADORES,
        default='i3',
    )
    
    hdd = models.CharField(
        verbose_name='Disco Duro',
        max_length=255,
        null=True,
    )
    
    ram = models.CharField(
        verbose_name='RAM',
        max_length=255,
        null=True,
    )
    
    mac = models.CharField(
        verbose_name='Mac',
        max_length=255,
        unique=True,
        default='mac'
    )
    
    t_video = models.BooleanField(
        verbose_name='Tarjeta de Video',
        default=False
    )
    
    t_red = models.BooleanField(
        verbose_name='Tarjeta de Red',
        default=False
    )
    
    detalles = models.TextField(
        verbose_name="Detalles",
        max_length=255,
        null=True,
        blank=True
    )