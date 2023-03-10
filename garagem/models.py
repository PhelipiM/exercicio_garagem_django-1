from django.db import models

class Marcas(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome.upper()

# Create your models here.
