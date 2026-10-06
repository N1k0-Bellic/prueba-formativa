from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    descripcion = models.TextField()
    impuesto_base = models.IntegerField(default=0)  # Campo numérico/monto

    def __str__(self):
        return f"{self.nombre} ({self.pais})"

class PaqueteTuristico(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='paquetes')
    nombre = models.CharField(max_length=100)
    dias = models.PositiveIntegerField()
    valor = models.IntegerField()  # Campo numérico de monto

    def __str__(self):
        return f"{self.nombre} - ${self.valor:,}"
