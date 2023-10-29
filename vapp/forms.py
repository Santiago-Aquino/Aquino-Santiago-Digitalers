from django import forms
from .models import *

# Importo el usuario de la otra aplicacion
from user.models import User


# Formulario Car
class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name', 'born', 'description',
                  'maximum_speed', 'image', 'company']


# Formulario Motorcycle
class MotorcycleForm(forms.ModelForm):

    class Meta:
        model = Motorcycle
        fields = ['name', 'born', 'description',
                  'maximum_speed', 'image', 'company']


# Formulario Bicycle
class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'born']


# Formulario Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


# Formulario User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']
