from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help' , views.help_me, name ='help_me')
]

