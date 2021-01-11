from django.shortcuts import render, HttpResponse, redirect
from .models import Pessoa
from .forms import PessoaForm

import requests
import os


def list_person(request):
    pessoas = Pessoa.objects.all().order_by('nome', 'sobrenome')
    return render(request, "pessoas/pessoas.html", {'pessoas': pessoas})


def generate_name(request):
    
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            return redirect('/pessoas/')
    else:
        response = requests.get(
            "https://gerador-nomes.herokuapp.com/nome/aleatorio")
        name_str = response.text
        name_str = name_str.replace(']', '')
        name_str = name_str.replace('[', '')
        name_str = name_str.replace('"', '')
        name_list = name_str.split(',')
        form = PessoaForm(
            initial={'nome': name_list[0] + ' ' + name_list[1], 'sobrenome': name_list[2]})
        data = {
            'name': name_list[0],
            'second_name': name_list[1],
            'last_name': name_list[2],
            'form': form
        }
        return render(request, "pessoas/pessoaCadastro.html", data)