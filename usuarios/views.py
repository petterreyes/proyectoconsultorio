from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout

from .forms import UserCreationForm, RolForm, RolUsuarioForm


# Create your views here.
from .models import User, Rol, RolUsuario


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect("index")



    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect("login")

def consultarusuarios(request, plantilla="consultarusuarios.html"):
    usuarios = User.objects.all
    return render(request, plantilla, {'usuarios':usuarios})

def consultarroles(request, plantilla="consultarroles.html"):
    roles = Rol.objects.all
    return render(request, plantilla, {'roles':roles})

def consultarrolesusuarios(request, plantilla="consultarrolesusuarios.html"):
    rolesusuarios = RolUsuario.objects.all
    return render(request, plantilla, {'rolesusuarios':rolesusuarios})

def crearusuario(request, plantilla="crearusuarios.html"):
    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('consultar_usuarios')
    else:
        form=UserCreationForm()
    return render(request, plantilla, {'form':form})

def crearrol(request, plantilla="crearrol.html"):
    if request.method=="POST":
        form = RolForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles')
    else:
        form=RolForm()
    return render(request, plantilla, {'form':form})

def crearrolusuario(request, plantilla="crearrolusuario.html"):
    if request.method=="POST":
        formRolUsuario = RolUsuarioForm(request.POST or None)
        if formRolUsuario.is_valid():
            formRolUsuario.save()
        return redirect('consultar_roles_usuarios')
    else:
        formRolUsuario=RolUsuarioForm()
    return render(request, plantilla, {'formRolUsuario':formRolUsuario})

def modificarusuario(request, pk, plantilla="modificarusuario.html"):
    if request.method=="POST":
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('consultar_usuarios')
    else:
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
    return render(request, plantilla, {'form':form})

def modificarrol(request, pk, plantilla="modificarrol.html"):
    if request.method=="POST":
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles')
    else:
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
    return render(request, plantilla, {'form':form})

def modificarrolusuario(request, pk, plantilla="modificarrolusuario.html"):
    if request.method=="POST":
        rolusuario = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles_usuarios')
    else:
        rolusuario = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
    return render(request, plantilla, {'form':form})


def eliminarusuario(request, pk, plantilla="eliminarusuario.html"):
    if request.method=="POST":
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
        if form.is_valid():
            usuario.delete()
        return redirect('consultar_usuarios')
    else:
        usuario = get_object_or_404(User, pk=pk)
        form = UserCreationForm(request.POST or None, instance=usuario)
    return render(request, plantilla, {'form':form})

def eliminarrol(request, pk, plantilla="eliminarrol.html"):
    if request.method=="POST":
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
        if form.is_valid():
            rol.delete()
        return redirect('consultar_roles')
    else:
        rol = get_object_or_404(Rol, pk=pk)
        form = RolForm(request.POST or None, instance=rol)
    return render(request, plantilla, {'form':form})

def eliminarrolusuario(request, pk, plantilla="eliminarrolusuario.html"):
    if request.method=="POST":
        rolusuario = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
        if form.is_valid():
            rolusuario.delete()
        return redirect('consultar_roles_usuarios')
    else:
        rolusuario = get_object_or_404(RolUsuario, pk=pk)
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
    return render(request, plantilla, {'form':form})