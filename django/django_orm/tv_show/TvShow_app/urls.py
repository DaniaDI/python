from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="show_index"),
    path('new/', views.show_new,name="show_new"),
    path('create/', views.show_create,name="show_create"),
    path('<int:id>/', views.show_read,name="show_read"),
    path('<int:id>/edit/', views.show_edit, name="edit_show"),
    path('<int:id>/update/', views.show_update, name="show_update"),
    path('<int:id>/destroy/', views.show_delete, name="show_delete"),
]
