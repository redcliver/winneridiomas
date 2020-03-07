from django.db import models
from django.utils import timezone

# Create your models here.
class contato(models.Model):
    VS = (
        ('1', 'Não Visualizado'),
        ('2', 'visualizado'),
    )
    id = models.AutoField(primary_key=True)
    visualizacao = models.CharField(max_length=1, choices=VS, default=1)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    mensagem = models.CharField(max_length=500)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class registro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email

class indicacao(models.Model):
    VS = (
        ('1', 'Não Visualizado'),
        ('2', 'visualizado'),
    )
    id = models.AutoField(primary_key=True)
    visualizacao = models.CharField(max_length=1, choices=VS, default=1)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200, null=True, blank=True)
    empresa = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    mensagem = models.CharField(max_length=500, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class testeNivelamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome