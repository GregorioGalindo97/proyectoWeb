from django.shortcuts import render
from contacto.models import Contacto

def contacto(request):
    contactos=Contacto.objects.all()
    return render(request,"contactos/contacto.html",{"contactos":contactos})
# Create your views here.
