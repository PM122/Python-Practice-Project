from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    thepass = ''

    if request.GET.get('uppercase'):
        alphabets.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        alphabets.extend(list('!@#$%^&*~'))

    if request.GET.get('numbers'):
        alphabets.extend(list(str(range(10))))

    for x in range(length):
        thepass += random.choice(alphabets)

    return render(request, 'generator/password.html', {"password": thepass})


def about(request):
    return render(request, 'generator/about.html')
