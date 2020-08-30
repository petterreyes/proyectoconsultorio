from django.shortcuts import render

# Create your views here.

def index(request, plantilla="index.html"):
    return render(request, plantilla)

def promociones(request, plantilla="promociones.html"):
    return render(request, plantilla)

def servicios(request, plantilla="servicios.html"):
    return render(request, plantilla)

def doctores(request, plantilla="doctores.html"):
    return render(request, plantilla)

def acerca(request, plantilla="acerca.html"):
    return render(request, plantilla)





