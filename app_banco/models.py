from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

TIPO_TRANSACAO = (
        ("D", "Debito"),
        ("C", "Credito"),
    )


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password,cpf, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        user = self.model(username=username, cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, cpf, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password,cpf, **extra_fields)

class CustomUser(AbstractUser):
    # Está classe está herdando da classe 'User' nativa do Django, o intuíto dessa herança é
    # para implementar  as variáveis 'data_nascimento' e 'cpf'
    data_nascimento = models.DateField(blank=True,null=True)
    cpf = models.IntegerField(unique=True)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.get_full_name())

class Conta(models.Model):
    cliente = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='cliente')
    numero = models.AutoField(unique=True, primary_key=True)
    limite = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.numero) +': ' + self.cliente.first_name

class Transacao(models.Model):
    conta = models.ForeignKey(Conta,on_delete=models.PROTECT,related_name='conta')
    tipo = models.CharField(max_length=1,choices=TIPO_TRANSACAO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)