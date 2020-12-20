from .models import CustomUser
from django.forms import ModelForm
from django import forms

class ClienteForm(forms.Form):
    usuario = forms.CharField(max_length=150)
    senha = forms.CharField(max_length=150, widget=forms.PasswordInput())
    primeiro_nome = forms.CharField(max_length=150)
    sobrenome = forms.CharField(max_length=150)
    cpf = forms.IntegerField()
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    saldo = forms.DecimalField(max_digits=10, decimal_places=2)
    limite = forms.DecimalField(max_digits=10, decimal_places=2)

class TransferenciaForm(forms.Form):
    numero_da_conta = forms.IntegerField()
    valor = forms.DecimalField(max_digits=10, decimal_places=2)