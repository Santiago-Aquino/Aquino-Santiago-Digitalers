from django.db import models

# Importo el Modelo usuario por defecto de Django
from django.contrib.auth.models import AbstractUser


# Creo mi propio modelo usuario con un campo image, heredando de la clase por defecto de user de Django
class User(AbstractUser):
    image = models.ImageField(upload_to='profile/',
                              null=True, blank=True, verbose_name='Imagen')
