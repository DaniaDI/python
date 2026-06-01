from django.shortcuts import render,redirect
from django.http import HttpResponse 

# Create your views here.
def index(request):
  return HttpResponse('placeholder to display all the surveys created')

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")