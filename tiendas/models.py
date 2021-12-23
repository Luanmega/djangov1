from django.db import models

class tiendas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre
