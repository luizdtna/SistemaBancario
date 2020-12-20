import decimal

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app_banco.models import CustomUser, Conta, Transacao
from .forms import ClienteForm, TransferenciaForm


# Create your views here.

def novo_cliente(request):
    # Aqui eu posso criar uma verificação se o usuário é staff

    form = ClienteForm(request.POST or None)

    if form.is_valid():
        # Cria um novo cliente
        novo_cliente = CustomUser.objects.create_user(username=request.POST['usuario'],
                                                      password=request.POST['senha'],
                                                      cpf=request.POST['cpf'],
                                                      first_name=request.POST['primeiro_nome'],
                                                      last_name=request.POST['sobrenome'],
                                                      data_nascimento=request.POST['data_nascimento'])

        # Cria uma conta e vincula ao novo cliente
        Conta.objects.create(cliente_conta=novo_cliente, saldo=request.POST['saldo'], limite=request.POST['limite'])

        return render(request, 'app_banco/novocliente.html', {'form': form, 'cliente_criado': True})
    return render(request, 'app_banco/novocliente.html', {'form': form})


@login_required()
def clienteTelaPrincipal(request):
    cliente = CustomUser.objects.get(pk=request.user.id)

    return render(request, 'app_banco/cliente_principal.html', {'cliente': cliente})

@login_required()
def confirmar_transferencia(request, id, valor):
    id_cliente_debitado = id

    form = TransferenciaForm(request.POST or None)
    erros = []
    try:
        cliente_creditado = Conta.objects.get(pk=request.user.cliente_conta.id)

        limite_maximo_transferencia = cliente_creditado.limite + cliente_creditado.saldo

        if float(limite_maximo_transferencia) < valor:
            erros.append('ERRO: O valor da transferência é maior que o limite e o saldo juntos')

        else:
            cliente_debitado = Conta.objects.get(pk=id_cliente_debitado)
            if cliente_creditado.id == id_cliente_debitado:
                erros.append('ERRO: Você está tentando se fazer uma transferência')
            else:
                saldo_em_falta = valor - float(cliente_creditado.saldo)

                if saldo_em_falta > 0:
                    cliente_creditado.saldo = 0
                    cliente_creditado.limite -= decimal.Decimal(saldo_em_falta)
                else:
                    cliente_creditado.saldo -= decimal.Decimal(valor)

                cliente_debitado.saldo += decimal.Decimal(valor)

                cliente_creditado.save()
                cliente_debitado.save()

                Transacao.objects.create(conta=cliente_debitado, tipo='D', valor=decimal.Decimal(valor))
                Transacao.objects.create(conta=cliente_creditado, tipo='C',
                                         valor=decimal.Decimal(valor)* -1)

                return render(request, 'app_banco/confirm_transferencia.html',
                              {'valor':valor, 'info_cliente_debitado': cliente_debitado, 'confirm': True})

        return render(request, 'app_banco/confirm_transferencia.html',
                      {'form': form, 'erros': erros})

    except Conta.DoesNotExist:
        erros.append('ERRO: Número de conta inválido')
        return render(request, 'app_banco/confirm_transferencia.html',
                      {'form': form, 'erros': erros})


@login_required()
def transferencia(request):
    form = TransferenciaForm(request.POST or None)
    erros = []
    try:
        if form.is_valid():
            cliente_debitado = Conta.objects.get(pk=form['numero_da_conta'].data)
            valor = form['valor'].data
            return render(request, 'app_banco/transferencia.html',
                          {'form': form, 'cliente_debitado': cliente_debitado, 'valor': valor})

        return render(request, 'app_banco/transferencia.html', {'form': form})
    except Conta.DoesNotExist:
        erros.append('ERRO: Número de conta inválido')
        return render(request, 'app_banco/confirm_transferencia.html',
                      {'form': form, 'erros': erros})


def my_logout(request):
    logout(request)
    return redirect('login')  # Indiquei uma URL da aplicação
