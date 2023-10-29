# Redirigir o renderizar
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect

# Vistas
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

# Mis formularios y modelos
from .forms import *
from .models import *
from user.models import User

# Para mostrar mensajes
from django.contrib import messages

# Formulario para el registro que otorga django
from django.contrib.auth.forms import UserCreationForm


# Vista Home
class HomeView(TemplateView):
    template_name = 'vapp/home.html'


# Vistas Cars
class CarCreate(CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('car-list')


class CarList(ListView):
    model = Car


def get_cars_by_name(request):
    # Aqui genero mi propia logica ya que preferi hacerlo a mi manera y no usar el model.objects.filter()
    query_name = request.GET.get('name').lower()
    cars_db = Car.objects.all()
    cars = []
    for car in cars_db:
        name_db = car.name.lower()[:10]
        if not name_db.find(query_name) == -1:
            cars.append(car)
    data = {'cars': cars}
    return render(request, 'vapp/car_list.html', data)


class CarUpdate(UpdateView):
    model = Car
    form_class = CarForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('car-update', args=[self.object.id]) + '?ok'


class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('car-list')


# Vistas Motorcycle
class MotorcycleCreate(CreateView):
    model = Motorcycle
    form_class = MotorcycleForm
    success_url = reverse_lazy('motorcycle-list')


class MotorcycleList(ListView):
    model = Motorcycle


def get_motorcycle_by_name(request):
    # Aqui genero mi propia logica ya que preferi hacerlo a mi manera y no usar el model.objects.filter()
    query_name = request.GET.get('name').lower()
    motorcycle_db = Motorcycle.objects.all()
    motorcycles = []
    for motorcycle in motorcycle_db:
        name_db = motorcycle.name.lower()[:10]
        if not name_db.find(query_name) == -1:
            motorcycles.append(motorcycle)
    data = {'motorcycles': motorcycles}
    return render(request, 'vapp/motorcycle_list.html', data)


class MotorcycleUpdate(UpdateView):
    model = Motorcycle
    form_class = MotorcycleForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('motorcycle-update', args=[self.object.id]) + '?ok'


class MotorcycleDelete(DeleteView):
    model = Motorcycle
    success_url = reverse_lazy('motorcycle-list')


# Vistas Company
class CompanyCreate(CreateView):
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('company-list')


class CompanyList(ListView):
    model = Company


def get_company_by_name(request):
    # Aqui genero mi propia logica ya que preferi hacerlo a mi manera y no usar el model.objects.filter()
    query_name = request.GET.get('name').lower()
    company_db = Company.objects.all()
    companies = []
    for company in company_db:
        name_db = company.name.lower()[:10]
        if not name_db.find(query_name) == -1:
            companies.append(company)
    data = {'companies': companies}
    return render(request, 'vapp/company_list.html', data)


class CompanyUpdate(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('company-update', args=[self.object.id]) + '?ok'


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('company-list')


# Comentarios
def create_comment(request):
    # Aqui genero mi propia logica y no uso Class Based View
    # Asi puedo guardar el usuario que esta logueado cuando crea el comentario
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data['text'], user=request.user.username)
            return HttpResponseRedirect(reverse('comment-list'))
    else:
        form = CommentForm()
        data = {'form': form}
        return render(request, 'vapp/comment_form.html', data)


def find_all_comments(request):
    # Aqui genero mi propia logica para traerme todos los datos
    comments = Comment.objects.all()
    data = {'comments': comments}
    return render(request, 'vapp/comment_list.html', data)


def get_comment_by_name(request):
    # Aqui genero mi propia logica ya que preferi hacerlo a mi manera y no usar el model.objects.filter()
    query_name = request.GET.get('name').lower()
    comments_db = Comment.objects.all()
    comments = []
    for comment in comments_db:
        name_db = comment.user.lower()[:10]
        if not name_db.find(query_name) == -1:
            comments.append(comment)
    data = {'comments_name': comments}
    return render(request, 'vapp/comment_list.html', data)


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('comment-update', args=[self.object.id]) + '?ok'


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment-list')


# Usuario: Registro / Login / Perfil
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('register'))
    else:
        form = UserCreationForm()
        data = {'form': form}
        return render(request, 'vapp/register.html', data)


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña inválidos")
        return self.render_to_response(self.get_context_data(form=form))


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('user-update', args=[self.object.id]) + '?ok'


# Acerca de mi
def get_about_me(request):
    return render(request, 'vapp/acerca.html')
