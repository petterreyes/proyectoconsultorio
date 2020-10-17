from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required


from .forms import UserCreationForm, RolForm, RolUsuarioForm
from django.db.models import Q

import io
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A5, A2, A3
from reportlab.lib.styles import *
from reportlab.lib.units import inch
from reportlab.platypus import *
from reportlab.lib.enums import TA_RIGHT, TA_CENTER


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


def consultarusuarios(request):
    buscar = request.GET.get("buscar")
    usuario = User.objects.all()

    if buscar:
        usuario = User.objects.filter(
            Q(username__icontains=buscar) |
            Q(email__icontains=buscar) |
            Q(date_of_birth__icontains=buscar)


        ).distinct()
    return render(request, 'consultarusuarios.html', {'usuarios':usuario})

#pdf de usuarios
@login_required(None, "", 'login')
def exportarListUsuarios(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_usuarios.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    usuarios = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de usuarios", styles['Heading1'])
    usuarios.append(header)
    headings = ('Usuario', 'Correo', 'Fecha de nacimiento')
    allusuarios = [(d.username, d.email, d.date_of_birth) for d in User.objects.all()]
    print
    allusuarios

    t = Table([headings] + allusuarios)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.yellowgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.yellowgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.yellowgreen)
        ]
    ))
    usuarios.append(t)
    doc.build(usuarios)
    response.write(buffer.getvalue())
    buffer.close()
    return response

def consultarroles(request):
    buscar = request.GET.get("buscar")
    roles = Rol.objects.all()

    if buscar:
        roles = Rol.objects.filter(
            Q(nombre__icontains=buscar)

        ).distinct()
    return render(request, 'consultarroles.html', {'roles':roles})

#pdf de roles
@login_required(None, "", 'login')
def exportarListRol(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_roles.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    roles = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de roles", styles['Heading1'])
    roles.append(header)
    headings = ('Id','Rol')
    allroles = [(d.id, d.nombre) for d in Rol.objects.all()]
    print
    allroles

    t = Table([headings] + allroles)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.thistle),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.thistle),
            ('BACKGROUND', (0, 0), (-1, 0), colors.thistle)
        ]
    ))
    roles.append(t)
    doc.build(roles)
    response.write(buffer.getvalue())
    buffer.close()
    return response


def consultarrolesusuarios(request, plantilla="consultarrolesusuarios.html"):
    rolesusuarios = RolUsuario.objects.all
    return render(request, plantilla, {'rolesusuarios':rolesusuarios})

#pdf de roles y usuarios
@login_required(None, "", 'login')
def exportarListRolUsuario(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_roles_usuarios.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    rolUsuario = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de roles y usuarios", styles['Heading1'])
    rolUsuario.append(header)
    headings = ('Rol','Usuario')
    allroles = [(d.rol, d.usuario) for d in RolUsuario.objects.all()]
    print
    allroles

    t = Table([headings] + allroles)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.steelblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.steelblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.steelblue)
        ]
    ))
    rolUsuario.append(t)
    doc.build(rolUsuario)
    response.write(buffer.getvalue())
    buffer.close()
    return response

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