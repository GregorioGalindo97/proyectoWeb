from django.shortcuts import redirect, render
from pedidos.models import Pedido,LineaPedido
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="/autenticacion/logear")

def procesar_pedidos(request):
    pedidos=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedidos
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(

        pedido=pedidos,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,

                 )


    messages.success(request,"El pedido se ha creado correctamente")
    return redirect("../home")


def enviar_mail(**kwagrs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{

        "pedido":kwagrs.get("pedido"),
        "lineas_pedido":kwagrs.get("lineas_pedido"),
        "nombreusuario":kwagrs.get("nombreusuario")
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="gregorio.galindo9711@hotmail.com"
    to="gregorio.galindo97@gmail.com"
    #kwagrs.get("email")

    send_mail(asunto, mensaje_texto,from_email,[to],html_message=mensaje)



# Create your views here.