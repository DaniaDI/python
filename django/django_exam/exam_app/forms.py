from django import  forms
from .models import User,Game
import re
from django.utils import timezone
from datetime import date  
# import bcrypt

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
            
    confirm_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
            
    class Meta:
        model=User
        fields = ['first_name', 'last_name', 'email', 'password','birthday']#birthday
       

   
    def clean_first_name(self):# problem title->unique
        typing = self.cleaned_data.get('first_name', '').strip()# give me the clean title or data user typing
        if len(typing) < 4:
          raise forms.ValidationError("firstName must be at least 4 characters long.")
        return typing

    def clean_last_name(self):# problem title->unique
            typing = self.cleaned_data.get('last_name', '').strip()# give me the clean title or data user typing
            if len(typing) < 4:
                raise forms.ValidationError("lastName must be at least 4 characters long.")
            return typing
    
    def clean_email(self):# problem title->unique
            typing = self.cleaned_data.get('email', '').strip()
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(typing):
                raise forms.ValidationError("Invalid email address!")
            if User.objects.filter(email=typing).exists():
                raise forms.ValidationError("Email already registered.")
            return typing
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # التحقق من شروط الباسورد وهو ما زال نصاً عادياً ونقياً
        if password and len(password) < 8:
            self.add_error('password', "Password must be at least 8 characters long.")

        # مقارنة حقل الباسورد بحقل تأكيد الباسورد
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        
        return cleaned_data
    
    # def clean_birthday(self):
    #     birthday = self.cleaned_data.get('birthday')
    #     if birthday and birthday >= timezone.now().date():
    #         raise forms.ValidationError("Birthday must be in the past.")
    #     return birthday

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if birthday and birthday >= date.today():
            raise forms.ValidationError("Birthday must be in the past.")
        return birthday

class LoginForm(forms.Form):  
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    def clean_email(self):
        typing = self.cleaned_data.get('email', '').strip()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(typing):
            raise forms.ValidationError("Invalid email address!")
        return typing
    
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'genre', 'release_date', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_name(self):
        typing = self.cleaned_data.get('name', '').strip()
        if len(typing) < 2:
            raise forms.ValidationError("Game Name must be at least 2 characters long.")
        return typing

    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if release_date and release_date >= date.today():
            raise forms.ValidationError("Release date must be in the past.")
        return release_date

    def clean_desc(self):
        typing = self.cleaned_data.get('desc', '').strip()
        if len(typing) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long.")
        return typing