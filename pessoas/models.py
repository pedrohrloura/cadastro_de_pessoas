from django.db import models
from django.contrib.auth import get_user_model
from django import forms

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.CharField(max_length=15)
    email = models.EmailField()
    apelido = models.CharField(max_length=15, blank=True)
    idade = models.IntegerField()
    data_nascimento = models.DateField('Data de nascimento (YYYY-MM-DD)')
    observacao=models.TextField(blank = True)


def __str__(self):
    return self.nome
