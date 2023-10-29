from django.contrib import admin
# Import los modelos
from .models import *

# Configuracion general
admin.site.site_title = 'Administrador de la pagina ViuVehicles'
admin.site.site_header = "Bienvenido/a administrador"
admin.site.index_title = "Administrador de la pagina ViuVehicles"


# Config de Compañía
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('name', 'born')
    ordering = ('born',)


# Config de Automóvil
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('name', 'born', 'description', 'maximum_speed')
    list_filter = ('company', 'born', 'maximum_speed')
    ordering = ('born',)


# Config de Motocicleta
class MotorcycleAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('name', 'born', 'description', 'maximum_speed')
    list_filter = ('company', 'born', 'maximum_speed')
    ordering = ('born',)


# Config de Comentario
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('text',)


# Agregando a la ruta admin/ los sig. modelos
admin.site.register(Company, CompanyAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Motorcycle, MotorcycleAdmin)
admin.site.register(Comment, CommentAdmin)
