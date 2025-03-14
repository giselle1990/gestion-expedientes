from django.db import models
from django.utils import timezone

# Create your models here.
# models.py
from django.db import models

class Expediente(models.Model):
    fecha = models.DateField()
    caratula = models.CharField(max_length=200)
    objeto = models.CharField(max_length=100)  # Campo más corto
    estado = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)  # Nuevo campo

    def __str__(self):
        return self.caratula