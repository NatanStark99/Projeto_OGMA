from django.db import models
from django.conf import settings


class Pergunta(models.Model):
    TIPO_QUADRANTE = [
        ('MUDAR','Mudar'),
        ('OBJETIVO','Objetivo'),
        ('FAZER_FLUIR','Fazer Fluir'),
        ('FAZER_MELHOR','Fazer Melhor')
    ]

    texto = models.TextField()
    quadrante = models.CharField(max_length=20,choices=TIPO_QUADRANTE)
    peso = models.FloatField(default=1.0)
    ordem = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['ordem']

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    valor = models.FloatField()
    coordenada_x = models.FloatField()
    coordenada_y = models.FloatField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        return f'Resposta {self.id} para {self.pergunta.texto[:50]}'