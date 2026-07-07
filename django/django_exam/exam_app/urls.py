
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='game_index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('game/create/',views.create_game,name='create_game'),
    path('game/<int:id>',views.edit_game,name='edit_game'),
    path('edit/game/<int:id>',views.update_game,name='update_game'),
    path('logout/', views.logout, name='logout'),
]
