from django.shortcuts import render

# Create your views here.
from cgitb import html
from django.http import HttpResponse


def home(request):
    return render(request, 'dsApp/index.html')