from django.http import HttpResponse
from django.shortcuts import HttpResponse, render
from carro.carro import Carro

def home(request):
    carro=Carro(request)
    return render(request,"proyectoWebApp/home.html")

