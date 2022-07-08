from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    imc_calculado = models.FloatField()

    def calcular_imc (self, altura,peso):
        self.imc_calculado = peso / (altura * altura)

