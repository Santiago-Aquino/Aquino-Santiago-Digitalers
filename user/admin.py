from django.contrib import admin

# Importo los modelos
from .models import User


# Config de Usuario
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', "last_name", "email")
    ordering = ('username',)


# Agregando a la ruta admin/ el sig. modelo
admin.site.register(User, UserAdmin)
