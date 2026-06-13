
from django.urls import path ,include
from . import views
urlpatterns = [
    path('', views.index,name='course_index'),
    path('course/<int:id>/destroy/', views.course_delete,name='course_delete'),
]
