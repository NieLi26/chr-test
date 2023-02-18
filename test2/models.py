from django.db import models

# Create your models here.


class Servicio(models.Model):
    '''Model definition for Service.'''
    numero = models.IntegerField()
    nombre = models.CharField(max_length=255, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    tipologia = models.CharField(max_length=255, blank=True)
    titular = models.CharField(max_length=255, blank=True)
    inversion = models.CharField(max_length=255, blank=True)
    fecha_ingreso = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)
    mapa = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        '''Meta definition for Service.'''

        ordering = ['id']

    def __str__(self):
        return self.nombre
    