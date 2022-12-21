from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=100)


class Ata(models.Model):
    participantes = models.ManyToManyField(Participante)
