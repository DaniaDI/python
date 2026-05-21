from django.urls import path
from . import views

urlpatterns = [
    path('redirect/', views.root, name='blog-root'),
    path('',views.index,name='blog_index'),
    path('new/',views.new,name='blog_new'),
    path('create/',views.create,name='blog_create'),
    path('<int:number>/',views.show,name='blog_show'),
    path('<int:number>/edit/',views.edit,name='blog_edit'),
    path('<int:number>/delete/', views.destroy, name='blog_destroy'),
    path('json/', views.json_response, name='blog_json'),
]
