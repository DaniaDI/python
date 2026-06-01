from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('save/',views.save,name='save'),
    path('show_table/',views.show_table,name='show_table'),
]
