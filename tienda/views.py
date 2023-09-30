from django.shortcuts import render,redirect
from  .forms import FormularioTienda
from django.core.mail import EmailMessage

def tienda(request):
    MiFormulario=FormularioTienda()
    if request.method=="POST":
        MiFormulario=FormularioTienda(data=request.POST)

        if MiFormulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app django",
                               "El usuario con nombre {} con la direccion {} escribe lo siguiente {}:\n\n" . format(nombre,email,contenido),
                               "",["gregorio.galindo9711@hotmail.com"],
                               reply_to=[email])
            
            try:
                email.send()
                return redirect("/tienda/?valido")
            except:
                return redirect("/tienda/?invalid")


        

    return render(request,"tiendas/tienda.html",{"miFormulario":MiFormulario})

