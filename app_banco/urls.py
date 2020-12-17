from django.urls import path
from django.views.generic.base import TemplateView
from .views import novo_cliente

urlpatterns = [
    path('',TemplateView.as_view(template_name='app_banco/home.html'), name='home_url'),

    path('gestao/',novo_cliente,name='gestao_url'),
]
