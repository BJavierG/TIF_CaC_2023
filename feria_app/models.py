from typing import Any
from django.db import models

# Create your models here.
class Producto(models.Model):
    cod         = models.CharField(max_length=6)
    articulo    = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    precio      = models.FloatField(blank=True, null=True)
    img         = models.CharField(max_length=100)

    class Meta:
        db_table = "productos_tabla"  

    def __str__(self):
        return f"El articulo {self.articulo} sale {self.precio}"
    
    def get_fields(self):
        return[
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]