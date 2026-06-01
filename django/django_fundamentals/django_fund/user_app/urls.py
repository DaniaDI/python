from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('users/new/', views.register, name='users_new'), # same method as register
    path('users/', views.index, name='users_index'),
]