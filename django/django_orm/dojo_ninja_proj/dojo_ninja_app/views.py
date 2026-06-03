from django.shortcuts import render,redirect
from .models import Dojo, Ninja
# Create your views here.
def index(request):
   context = {
        'dojos': Dojo.objects.all()# ninjas من خلال dojo ,related_name=ninjas
    }
   return render(request, 'index.html', context)
  

def add_dojo(request):
    if request.method == 'POST':
        name=request.POST['name']
        city  = request.POST['city']
        state = request.POST['state']
       
        Dojo.objects.create(
            name  = name,
            city  = city,
            state = state,
            desc  = 'new_dojo',
        )
    return redirect('/')
def add_ninja(request):
    if request.method == 'POST':
        f_name=request.POST['first_name']
        l_name  = request.POST['last_name']
        dojo_id  = request.POST['dojo_id']
        Ninja.objects.create(
            first_name  = f_name,
            last_name  = l_name,
            dojo = Dojo.objects.get(id=dojo_id),
          
        )
    return redirect('/')

def delete_dojo(request,id):
    if request.method == 'POST':
      Dojo.objects.get(id=id).delete()  # ← بتحذف الـ dojo + كل ninjas تبعه
    return redirect('/')