from django.urls import path
from django.views.generic.base import TemplateView
from .views import novo_cliente, clienteTelaPrincipal

urlpatterns = [
    path('',TemplateView.as_view(template_name='app_banco/index.html'), name='index_url'),

    path('gestao/',novo_cliente,name='gestao_url'),
    path('home/',clienteTelaPrincipal,name='home_url')
]
