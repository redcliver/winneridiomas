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
    sobrenome = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=300, null=True, blank=True)
    mensagem = models.CharField(max_length=500)
    data_cadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome