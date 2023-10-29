from django.db import models


# Modelo de compañía
class Company(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name='Empresa')
    born = models.IntegerField(
        null=False, blank=False, verbose_name='Año de fundación')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


# Modelo de Automovil
class Car(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name='Automóvil')
    born = models.IntegerField(
        null=False, blank=False, verbose_name='Año de creación')
    description = models.TextField(
        null=False, blank=False, verbose_name='Descripción')
    maximum_speed = models.IntegerField(
        null=True, blank=True, verbose_name='Velocidad Maxima')
    image = models.ImageField(
        upload_to='vehicles/', null=True, blank=True, verbose_name='Imagen')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Automóvil"
        verbose_name_plural = "Automóviles"


# Modelo de Motocicleta
class Motorcycle(models.Model):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name='Motocicleta')
    born = models.IntegerField(null=False, blank=False,
                               verbose_name='Año de creación')
    description = models.TextField(
        null=False, blank=False, verbose_name='Descripción')
    maximum_speed = models.IntegerField(
        null=True, blank=True, verbose_name='Velocidad Maxima')
    image = models.ImageField(upload_to='vehicles/',
                              null=True, blank=True, verbose_name='Imagen')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Motocicleta"
        verbose_name_plural = "Motocicletas"


# Modelo de Comentario
class Comment(models.Model):
    text = models.TextField(null=False, blank=False, verbose_name='Comentario')
    user = models.CharField(max_length=50, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:80]+'...'

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
