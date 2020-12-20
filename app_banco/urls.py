from django.urls import path
from django.views.generic.base import TemplateView
from .views import novo_cliente, clienteTelaPrincipal, transferencia, confirmar_transferencia

urlpatterns = [

    path('gestao/',novo_cliente,name='gestao_url'),
    path('transferencia/', transferencia,name='transferencia_url'),
    path('confirmacao/<int:id>/<int:valor>/',confirmar_transferencia, name='confirmacao_url'),
    path('',clienteTelaPrincipal,name='home_url'),

]
