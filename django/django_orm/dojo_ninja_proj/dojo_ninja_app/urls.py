from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='dojo_index'),
    path('add_dojo/', views.add_dojo, name='add_dojo'),
    path('add_ninja/', views.add_ninja, name='add_ninja'),
    path('delete/<int:id>/', views.delete_dojo, name='delete_dojo'),

]