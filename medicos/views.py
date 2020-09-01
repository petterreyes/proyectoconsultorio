from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import MedicosForm, Medicos

# Create your views here.
def medico(request, plantilla="medicos.html"):
    medicos = Medicos.objects.all()
    data = {
        'medico':medicos
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearmedicos(request, plantilla="crearmedicos.html"):

    if request.method == "POST":
        form = MedicosForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('medicos')
    else:
        form = MedicosForm

    return render(request, plantilla, {'form': form})

#pagina de crear o insertar INSERT
def modificarmedicos(request, pk, plantilla="modificarmedicos.html"):

    if request.method == "POST":
        form = MedicosForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('medicos')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)

    return render(request, plantilla, {'form': form})


def eliminarmedicos(request, pk, plantilla="eliminarmedicos.html"):

    if request.method == "POST":
        form = MedicosForm((request.POST or None))
        medico = get_object_or_404(Medicos, pk=pk)
        if form.is_valid():
            medico.delete()
            return redirect('medicos')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)

    return render(request, plantilla, {'form': form})