from django.shortcuts import render, HttpResponse
from.models import Pessoa

import requests
import os

def list_person(request):
    pessoas = Pessoa.objects.all()
    return render(request, "pessoas/pessoas.html",{'pessoas':pessoas})


def generate_name(request):
    response = requests.get("https://gerador-nomes.herokuapp.com/nome/aleatorio")
    name_str = response.text
    name_str = name_str.replace(']','')
    name_str = name_str.replace('[','')
    name_str = name_str.replace('"','')
    name_list = name_str.split(',')
    data = {
        'name':name_list[0],
        'second_name':name_list[1],
        'last_name':name_list[2]
    }
    return render(request, "pessoas/pessoaCadastro.html",data)

