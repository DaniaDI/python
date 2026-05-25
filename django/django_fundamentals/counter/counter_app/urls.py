from django.urls import path,include
from . import views

urlpatterns = [
    
path('' , views.index , name='counter_index'),
path('destroy_session/' , views.destroy , name='destroy_session'),
path('add2/' , views.add2 , name='add2'),
path('add_custom/' , views.add_custom , name='add-_custom'),
]
