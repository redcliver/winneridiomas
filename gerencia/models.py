from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class alunoModel(models.Model):
    ES = (
        ('1', 'Ativo'),
        ('2', 'Bloqueado'),
        ('3', 'Inativo'),
    )
    user = models.OneToOneField(User, on_delete="models.CASCADE")
    liberacao = models.CharField(max_length=1, choices=ES, default=1)
    nome = models.CharField(max_length=300, null=True, blank=True)
    sobrenome = models.CharField(max_length=400, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=400, null=True, blank=True)
    numero = models.CharField(max_length=5, null=True, blank=True)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    classe = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    dataNasc = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nome