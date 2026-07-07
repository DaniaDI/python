from django.db import models


# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True,unique=True)
    password=models.CharField(max_length=255,null=True)
    birthday = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Game(models.Model):
    GENRE_CHOICES = [
            ('Action', 'Action'),
            ('RPG', 'RPG'),
            ('Arcade', 'Arcade'),
            ('Strategy', 'Strategy'),
            ('Adventure', 'Adventure'),
     ]
    
    name=models.CharField(max_length=255,null=True)
    genre =models.CharField(max_length=255, choices=GENRE_CHOICES, null=True)
    desc=models.TextField()
    release_date=models.DateField(null=True)
    created_by= models.ForeignKey(User, related_name = "games_created", on_delete = models.CASCADE)
    players_who_like=models.ManyToManyField(User,related_name="liked_games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name