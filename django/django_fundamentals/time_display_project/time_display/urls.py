from django.urls import path
from . import views
urlpatterns = [
    path('',views.index , name='time_index'),
    path('time/',views.time_view , name='time_view'),
]
