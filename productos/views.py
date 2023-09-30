from django.shortcuts import render
from productos.models import Producto

def productos(request):

    productos=Producto.objects.all()
    return render(request,"productos/productos.html",{"productos":productos})
# Create your views here.

