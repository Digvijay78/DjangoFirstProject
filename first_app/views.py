from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {
        'insert_me' : "Hello i am from views.py"
    }
    return render(request, 'first_app/index.html', context = my_dict)

def help_me(request):
    my_help = {
        'insert_me' : "HI i am from views.py"
    }
    return render(request, 'first_app/help.html', context = my_help)