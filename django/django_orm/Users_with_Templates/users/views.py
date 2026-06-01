from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def index(request):
    # username=request.POST['name']
    # request.session['name'] = username

    # email=request.POST['email']
    # request.session['email'] = email

    # age=request.POST['age']
    # request.session['age'] = age

    
    return render(request,'index.html')

def save(request):
    if request.method=='POST':

         f_name = request.POST['first_name']
         l_name = request.POST['last_name']
        # دمج الاسمين معاً ليصبح الاسم الكامل
         full_name = f"{f_name} {l_name}"
         form_email = request.POST['email']
         form_age = request.POST['age']
            
        
         User.objects.create(name=full_name, email=form_email, age=form_age)
         return redirect('/')
    
    return redirect('/')


def show_table(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, 'table.html', context)