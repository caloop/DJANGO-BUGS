from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def portifolio(request):
    return render(request, 'portifolio.html')

