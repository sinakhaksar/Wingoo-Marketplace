from django.urls import path
from . import views

app_name= 'dashbord'

urlpatterns= [
    path('', views.index, name='index'),
]