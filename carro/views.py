from django.shortcuts import redirect
from .carro import Carro
from productos.models import Producto

def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Productos")

def eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Productos")

def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Productos")

def limpiar_carro(request,producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Productos")