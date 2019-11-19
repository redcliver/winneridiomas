from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class cidadeModel(models.Model):
    LB = (
        ('1', 'Ativa'),
        ('2', 'Bloqueada'),
        ('3', 'Inativa'),
    )
    ES = (
        ('01', 'Acre (AC)'),
        ('02', 'Alagoas (AL)'),
        ('03', 'Amapá (AP)'),
        ('04', 'Amazonas (AM)'),
        ('05', 'Bahia (BA)'),
        ('06', 'Ceará (CE)'),
        ('07', 'Distrito Federal (DF)'),
        ('08', 'Espírito Santo (ES)'),
        ('09', 'Goiás (GO)'),
        ('10', 'Maranhão (MA)'),
        ('11', 'Mato Grosso (MT)'),
        ('12', 'Mato Grosso do Sul (MS)'),
        ('13', 'Minas Gerais (MG)'),
        ('14', 'Pará (PA)'),
        ('15', 'Paraíba (PB)'),
        ('16', 'Paraná (PR)'),
        ('17', 'Pernambuco (PE)'),
        ('18', 'Piauí (PI)'),
        ('19', 'Rio de Janeiro (RJ)'),
        ('20', 'Rio Grande do Norte (RN)'),
        ('21', 'Rio Grande do Sul (RS)'),
        ('22', 'Rondônia (RO)'),
        ('23', 'Roraima (RR)'),
        ('24', 'Santa Catarina (SC)'),
        ('25', 'São Paulo (SP)'),
        ('26', 'Sergipe (SE)'),
        ('27', 'Tocantins (TO)'),
    )
    liberacao = models.CharField(max_length=2, choices=LB, default='1')
    nome = models.CharField(max_length=300, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ES, default='12')
    dataCadastro = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nome

class colaboradorModel(models.Model):
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
    cidadeEstado = models.ForeignKey(cidadeModel, on_delete="models.CASCADE")
    cep = models.CharField(max_length=10, null=True, blank=True)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    dataNasc = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nome

class salaModel(models.Model):
    ES = (
        ('1', 'Ativa'),
        ('2', 'Bloqueada'),
        ('3', 'Inativa'),
    )
    liberacao = models.CharField(max_length=1, choices=ES, default=1)
    nome = models.CharField(max_length=300, null=True, blank=True)
    localizacao = models.CharField(max_length=300, null=True, blank=True)
    capacidade = models.CharField(max_length=3, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    cidadeEstado = models.ForeignKey(cidadeModel, on_delete="models.CASCADE")
    cep = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.nome


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
    cidadeEstado = models.ForeignKey(cidadeModel, on_delete="models.CASCADE")
    cep = models.CharField(max_length=10, null=True, blank=True)
    salaAula = models.ForeignKey(salaModel, on_delete="models.CASCADE")
    telefone = models.CharField(max_length=14, null=True, blank=True)
    celular = models.CharField(max_length=14, null=True, blank=True)
    dataNasc = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
