from django.shortcuts import render, redirect
from .forms import Serviciosform, Servicios

# Create your views here.
def servicio(request, plantilla="consultarservicios.html"):
    servicios = Servicios.objects.all()
    data = {
        'servicio':servicios
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearservicios(request, template_name="crearservicios.html"):

    if request.method == "POST":
        form = Serviciosform(request.POST)
        if form.is_valid():
            form.save()
            redirect('servicios')
    else:
        form = Serviciosform

    return render(request, template_name, {'servicios':form})
