from django import forms
from django.forms import ModelForm


from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome','sobrenome','email','apelido','idade','data_nascimento','observacao')
