from django.contrib import admin
from app_banco.models import CustomUser, Conta, Transacao
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Conta)
admin.site.register(Transacao)