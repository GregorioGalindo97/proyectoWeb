from django.db import models

class Contacto(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='contacto')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='contacto'
        verbose_name='contactos'

    def __str__(self):
        return self.titulo

# Create your models here.
