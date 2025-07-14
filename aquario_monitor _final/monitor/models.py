from django.db import models
from django.utils import timezone

class SensorData(models.Model):
    temperatura = models.FloatField()
    sujidade = models.FloatField()
    sistema_ligado = models.BooleanField()
    aquecedor_ligado = models.BooleanField()
    emergencia_ativa = models.BooleanField()
    alerta_sujidade = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Dados em {self.timestamp}"