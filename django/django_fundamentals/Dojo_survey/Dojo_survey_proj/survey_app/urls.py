from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dojo_form'),   
    path('result/', views.result, name='result'),
]
