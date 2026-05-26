from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('guess/', views.guess, name='guess'),
    path('restart/', views.restart, name='restart'),
    path("save_score/", views.save_score, name="save_score"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
]
