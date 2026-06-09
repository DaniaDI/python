from django.urls import path 
from . import views


urlpatterns = [
    path('', views.add_book, name='author_book_index'),
    path('add_book/', views.add_book,name='add_book'),
    path('books/<int:id>/', views.view_book, name='book_detail'),
    path('add_author/', views.add_author,name='add_author'),
    path('authors/<int:id>/', views.view_author, name='view_author'),
]


