from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from datetime import date
# Create your models here.

def validate_title_length(value):
    if len(value.strip()) < 2:
        raise ValidationError("This field must be at least 2 characters long.")
   

# 1. Ninja Bonus:  date in past:
def validate_date_in_past(value):
    if value >= date.today():
        raise ValidationError("Release date must be in the past.")

def validate_description_length(value):
    typing = value.strip()
    # الفحص يعمل فقط إذا كان المستخدم قد كتب  بالفعل في الحقل
    if len(typing) > 0 and len(typing) < 10:
        raise ValidationError("Description is optional, but if provided, it must be at least 10 characters long.")
    
class Show(models.Model):
    title = models.CharField(max_length=255,null=True, unique=True, validators=[validate_title_length])
             
    network = models.CharField(max_length=45,null=True, validators=[MinLengthValidator(3, message="This field must be at least 3 characters long.")])
            
    release_date = models.DateField(validators=[validate_date_in_past])
       
    desc = models.TextField(null=True, blank=True ,validators=[validate_description_length])           
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

def __str__(self):
    return self.title