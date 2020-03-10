from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class imagensModel(models.Model):
  image = CloudinaryField('image')

class eventoModel(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    local_evento = models.CharField(max_length=1000, null=True, blank=True)
    conteudo = models.CharField(max_length=2000, null=True, blank=True)
    imagem_capa = CloudinaryField('image')
    imagem_adicional = models.ManyToManyField(imagensModel)
    data_publicacao = models.DateTimeField(default=timezone.now)
    data_evento = models.DateField(null=True, blank=True)
    hora_evento = models.TimeField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
