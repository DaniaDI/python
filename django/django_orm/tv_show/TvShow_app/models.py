from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255,null=True)
    network = models.CharField(max_length=45,null=True)
    release_date = models.DateField()
    desc = models.TextField(null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

def __str__(self):
    return self.title