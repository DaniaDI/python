

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User , Game
from .forms import RegisterForm, LoginForm ,GameForm
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect('dashboard')

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
                return redirect('dashboard')
                
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
                        return redirect('dashboard')
                
                messages.error(request, "Invalid Email or Password")

    context = {
        'reg_form': reg_form,
        'login_form': login_form
    }
    return render(request, 'index.html', context)


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('game_index')
    
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.created_by = User.objects.get(id=request.session['user_id'])
            game.save()
            game.players_who_like.add(game.created_by)
            return redirect('dashboard')
    else:
        form = GameForm()
        
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'form': form,
        'all_games': Game.objects.all()
    }
    return render(request, 'dashboard.html', context)

def edit_game(request,id):
    if 'user_id' not in request.session:  # ← Authorization
        messages.warning(request, "Please log in to access this page.")
        return redirect('game_index')
    
    user_id=request.session['user_id']
    user_logged =User.objects.get(id=user_id)
    game=Game.objects.get(id=id)
    form=GameForm(instance=game)

    if request.method == 'POST':
        form_type=request.POST.get('form_type')
        if form_type =='edit'and game.created_by.id == user_logged.id:
        
            form=GameForm(request.POST,instance=game)
            if form.is_valid():
                game=form.save(commit=False)
                game.created_by=user_logged
                game.save()
                game.players_who_like.add(user_logged)
                return redirect('edit_game')
        # elif form_type == 'delete' and game.created_by.id == user_logged.id:
        #         form = GameForm(request.POST, instance=game)
        #         game.delete()
        #         return redirect('dashboard')
    context={
            'form':form,
            'game':game,
            'user':user_logged
        }
    return render(request,'update.html',context)
        
def update_game(request,id):
    
    if 'user_id' not in request.session:  # ← Authorization
        messages.warning(request, "Please log in to access this page.")
        return redirect('game_index')
    
    user_id=request.session['user_id']
    user_logged =User.objects.get(id=user_id)
    game=Game.objects.get(id=id)
    form=GameForm(instance=game)

    if request.method == 'POST':
        form_type=request.POST.get('form_type')
        if form_type =='apply':
        
            form=GameForm(request.POST,instance=game)
            if form.is_valid():
                game=form.save(commit=False)
                game.created_by=user_logged
                game.save()
                game.players_who_like.add(user_logged)
                return redirect('edit_game',id=game.id)
            
        elif form_type == 'cancel' :
                return redirect('edit_game',id=game.id)
        
        elif form_type == 'delete' :
                game.delete()
                return redirect('dashboard')
    context={
            'form':form,
            'game':game,
            'user':user_logged
        }
    return render(request,'update.html',context)
def logout(request):
    request.session.clear()  # ← يمسح كل الـ session
    messages.info(request, "You have been logged out successfully.")
    return redirect('game_index')
