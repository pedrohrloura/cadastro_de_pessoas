from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=15)
    email = models.EmailField()
    apelido = models.CharField(max_length=15)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    observacao = models.TextField()

def __str__(self):
    return self.nome
