from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class eventoModel(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=500, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    conteudo = models.CharField(max_length=2000, null=True, blank=True)
    imagemCapa = CloudinaryField('eventos')
    imagem1 = models.ImageField(default='media/default.png', blank=True)
    imagem2 = models.ImageField(default='media/default.png', blank=True)
    imagem3 = models.ImageField(default='media/default.png', blank=True)
    imagem4 = models.ImageField(default='media/default.png', blank=True)
    imagem5 = models.ImageField(default='media/default.png', blank=True)
    imagem6 = models.ImageField(default='media/default.png', blank=True)
    imagem7 = models.ImageField(default='media/default.png', blank=True)
    imagem8 = models.ImageField(default='media/default.png', blank=True)
    imagem9 = models.ImageField(default='media/default.png', blank=True)
    imagem10 = models.ImageField(default='media/default.png', blank=True)
    dataEvento = models.DateTimeField(default=timezone.now())
    dataCadastro = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.titulo
