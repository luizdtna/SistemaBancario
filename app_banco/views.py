from django.shortcuts import render, redirect
from app_banco.models import CustomUser, Conta
from .forms import ClienteForm

# Create your views here.

def novo_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        novo_cliente = CustomUser.objects.create_user(username=request.POST['usuario'],
                                       password=request.POST['senha'],
                                       cpf=request.POST['cpf'],
                                       first_name=request.POST['primeiro_nome'],
                                       last_name=request.POST['sobrenome'],
                                       data_nascimento=request.POST['data_nascimento'])
        Conta.objects.create(cliente=novo_cliente,saldo=request.POST['saldo'], limite=request.POST['limite'])

        return render(request, 'app_banco/novocliente.html', {'form': form, 'cliente_criado': True})
    return render(request, 'app_banco/novocliente.html', {'form': form})
