from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class eventoModel(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    conteudo = models.CharField(max_length=2000, null=True, blank=True)
    imagem_capa = CloudinaryField('image')
    imagem = CloudinaryField('image')
    data_publicacao = models.DateTimeField(default=timezone.now())
    data_evento = models.DateTimeField(default=timezone.now())
    data_cadastro = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.titulo

class Photo(models.Model):
  image = CloudinaryField('image')