from django.db import models

# Create your models here.

class Edificio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    opciones_tipo=(
        ('Residencial','residencial'),
        ('Comercial','comercial'),
        )

    tipo = models.CharField(max_length=20, choices=opciones_tipo)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

class Departamento(models.Model):
    nombre_completo = models.CharField(max_length=30)
    costo = models.IntegerField()
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="num_edificio")

    def __str__(self):
        return "%s %s %s %s" % (self.nombre_completo,
                self.costo,
                self.num_cuartos,
                self.edificio)