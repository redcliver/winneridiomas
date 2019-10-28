from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class eventoModel(models.Model):
    name= models.CharField(max_length=500)
    imagem = CloudinaryField('imagem')

    def __str__(self):
        return self.name

class Photo(models.Model):
  image = CloudinaryField('image')