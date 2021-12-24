from django.db import models
from django.utils import timezone

class Productos(models.Model):
    class Meta:
        verbose_name_plural = "Productos"
    
    tienda = models.ForeignKey('tiendas.tiendas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    area = models.CharField(max_length=100)
    identificador = models.IntegerField()

    def __str__(self):
        return self.nombre