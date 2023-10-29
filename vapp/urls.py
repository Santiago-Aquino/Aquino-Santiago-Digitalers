from django.urls import path
from .views import *

urlpatterns = [
    # Car
    path('', HomeView.as_view(), name='home'),
    path('car-create/', CarCreate.as_view(), name='car-create'),
    path('car-list/', CarList.as_view(), name='car-list'),
    path('car-list-name/', get_cars_by_name, name='cars-name'),
    path('car-update/<int:pk>', CarUpdate.as_view(), name='car-update'),
    path('car-delete/<int:pk>', CarDelete.as_view(), name='car-delete'),

    # Motorcycle
    path('motorcycle-create/', MotorcycleCreate.as_view(),
         name='motorcycle-create'),
    path('motorcycle-list/', MotorcycleList.as_view(), name='motorcycle-list'),
    path('motorcycle-list-name/', get_motorcycle_by_name, name='motorcycle-name'),
    path('motorcycle-update/<int:pk>',
         MotorcycleUpdate.as_view(), name='motorcycle-update'),
    path('motorcycle-delete/<int:pk>',
         MotorcycleDelete.as_view(), name='motorcycle-delete'),

    # Company
    path('company-create/', CompanyCreate.as_view(), name='company-create'),
    path('company-list/', CompanyList.as_view(), name='company-list'),
    path('company-list-name/', get_company_by_name, name='company-name'),
    path('company-update/<int:pk>', CompanyUpdate.as_view(), name='company-update'),
    path('company-delete/<int:pk>', CompanyDelete.as_view(), name='company-delete'),

    # Comment
    path('comment-create/', create_comment, name='comment-create'),
    path('comment-list/', find_all_comments, name='comment-list'),
    path('comment-list-name/', get_comment_by_name, name='comment-name'),
    path('comment-update/<int:pk>/',
         CommentUpdate.as_view(), name='comment-update'),
    path('comment-delete/<int:pk>', CommentDelete.as_view(), name='comment-delete'),

    # Usuarios registro / login / logout
    path('register/', register, name='register'),
    path('login/',  MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name="user-update"),

    # Acerca de mi
    path('about-me', get_about_me, name='about-me'),
]
