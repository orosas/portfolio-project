from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Título', max_length=255)
    pub_date = models.DateTimeField('Fecha De Publicación',)
    body = models.TextField('Mensaje Blog')
    image = models.ImageField('Imagen',upload_to='images/')