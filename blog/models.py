from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField('Título', max_length=255)
    pub_date = models.DateTimeField('Fecha De Publicación',)
    body = models.TextField('Mensaje Blog')
    image = models.ImageField('Imagen',upload_to='images/')

    # Omar: En video curso se inserta la siguiente función para
    # truncar el text presentado en template blog/allblogs.html
    # y haciendo llamado a la función de la forma:
    # {{ blog.summary }}
    # pero sustituí la llamada, por la built-in tag:
    # {{ blog.body|truncatechars:100 }}

    # def summary(self):
    #     return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d-%B-%Y')

    def __str__(self):
        return self.title