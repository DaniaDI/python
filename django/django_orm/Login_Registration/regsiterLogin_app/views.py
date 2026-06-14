from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import RegisterForm, LoginForm
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect('/success')

    reg_form = RegisterForm()
    login_form = LoginForm()

    if request.method == 'POST':
        
        form_type = request.POST.get('form_type')# input hidden 
        if 'register' in form_type:# value of input hidden
            reg_form = RegisterForm(request.POST) 
            if reg_form.is_valid():
                user = reg_form.save(commit=False)
                password = reg_form.cleaned_data['password']
                user.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user.save()
            
                request.session['user_id'] = user.id # سجل دخول
                
                # messages.success(request, f"Welcome {user.first_name}! Your account was created successfully.")
                return redirect('success')
                
        elif 'login' in form_type:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email_input = login_form.cleaned_data['email']#clean_data from clean(def) inj forms.py 
                password_input = login_form.cleaned_data['password']
                user_list = User.objects.filter(email__iexact=email_input)
                
                if user_list:
                    logged_user = user_list[0]
                    #
                    if bcrypt.checkpw(password_input.encode(), logged_user.password.encode()):
                        request.session['user_id'] = logged_user.id
                        return redirect('success')
                
                messages.error(request, "Invalid Email or Password")

    context = {
        'reg_form': reg_form,
        'login_form': login_form
    }
    return render(request, 'index.html', context)


def success(request):
    if 'user_id' not in request.session:  # ← Authorization
        messages.warning(request, "Please log in to access this page.")
        return redirect('index')
    
    user_id=request.session['user_id']
    user = User.objects.get(id=user_id)
    context={
        'user':user
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.clear()  # ← يمسح كل الـ session
    messages.info(request, "You have been logged out successfully.")
    return redirect('index')