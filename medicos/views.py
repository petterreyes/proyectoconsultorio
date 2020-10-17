import io
from io import BytesIO

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A5, A2, A3
from reportlab.lib.styles import *
from reportlab.lib.units import inch
from reportlab.platypus import *
from reportlab.lib.enums import TA_RIGHT, TA_CENTER


from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


#pdf de medicos
@login_required(None, "", 'login')
def exportarListMedicos(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_medicos.pdf"'

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

    medicos = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de medicos", styles['Heading1'])
    medicos.append(header)
    headings = ('Apellido', 'Nombres', 'Edad', 'Email', 'Sexo')
    allmedicos = [(d.apellido, d.nombre, d.edad, d.email, d.sexo) for d in Medicos.objects.all()]
    print
    allmedicos

    t = Table([headings] + allmedicos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    medicos.append(t)
    doc.build(medicos)
    response.write(buffer.getvalue())
    buffer.close()
    return response


#consulta de medicos
@login_required(None, "", 'login')
def medico(request):
    buscar = request.GET.get("buscar")
    medicos = Medicos.objects.all()
    if buscar:
        medicos = Medicos.objects.filter(
            Q(apellido__icontains=buscar) |
            Q(nombre__icontains=buscar) |
            Q(especialidad__icontains=buscar) |
            Q(edad__icontains=buscar) |
            Q(sexo__icontains=buscar) |
            Q(email__icontains=buscar)
        ).distinct()
    return render(request, 'medicos.html', {'medico':medicos})


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

#pagina de modificar
def modificarmedicos(request, pk, plantilla="modificarmedicos.html"):
    if request.method == "POST":
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)
        if form.is_valid():
            form.save()
        return redirect('medicos')
    else:
        medico = get_object_or_404(Medicos, pk=pk)
        form = MedicosForm(request.POST or None, instance=medico)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
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

#consulta de USUARIOS
def consultarusuario(request, plantilla="consultarusuario.html"):
    usuario = Usuario.objects.all()
    data = {
        'usuario':usuario
    }
    return render(request, plantilla, data)

#pagina de crear o insertar INSERT
def crearusuario(request, plantilla="crearusuarios.html"):

    if request.method == "POST":
        form = UsuarioForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarusuario(request, pk, plantilla="modificarusuario.html"):
    if request.method == "POST":
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('usuario')
    else:
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarusuario(request, pk, plantilla="eliminarusuario.html"):

    if request.method == "POST":
        form = UsuarioForm((request.POST or None))
        usuario = get_object_or_404(Usuario, pk=pk)
        if form.is_valid():
            usuario.delete()
            return redirect('usuario')
    else:
        usuario = get_object_or_404(Usuario, pk=pk)
        form = UsuarioForm(request.POST or None, instance=usuario)

    return render(request, plantilla, {'form': form})

#pdf de paciente
@login_required(None, "", 'login')
def exportarListPaciente(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Pacientes.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A3)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consultarpaciente = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Pacientes ", styles['Heading1'])
    consultarpaciente.append(header)
    headings = ('Nombres', 'Apellido', 'Fecha de nacimiento', 'Cedula', 'Edad', 'Email', 'Sexo','Estado Civil', 'Telefono')
    allpaciente = [(d.nombre,d.apellido, d.fecha_nacimiento, d.cedula, d.edad, d.email, d.sexo, d.estado_civil, d.telefono) for d in Paciente.objects.all()]
    print
    allpaciente

    t = Table([headings] + allpaciente)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarpaciente.append(t)
    doc.build(consultarpaciente)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#paciente
def consultarpaciente(request):
    buscar = request.GET.get("buscar")
    pacientes = Paciente.objects.all()
    if buscar:
        pacientes = Paciente.objects.filter(
            Q(nombre__icontains=buscar) |
            Q(apellido__icontains=buscar) |
            Q(fecha_nacimiento__icontains=buscar) |
            Q(cedula__icontains=buscar) |
            Q(edad__icontains = buscar) |
            Q(email__icontains=buscar) |
            Q(sexo__icontains=buscar) |
            Q(estado_civil__icontains=buscar)|
            Q(telefono__icontains=buscar)
        ).distinct()
    return render(request, 'consultarpaciente.html', {'paciente':pacientes})

#pagina de crear o insertar INSERT
def crearpaciente(request, plantilla="crearpaciente.html"):

    if request.method == "POST":
        form = PacienteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('paciente')
    else:
        form = PacienteForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarpaciente(request, pk, plantilla="modificarpaciente.html"):
    if request.method == "POST":
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)
        if form.is_valid():
            form.save()
        return redirect('paciente')
    else:
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarpaciente(request, pk, plantilla="eliminarpaciente.html"):

    if request.method == "POST":
        form = PacienteForm((request.POST or None))
        paciente = get_object_or_404(Paciente, pk=pk)
        if form.is_valid():
            paciente.delete()
            return redirect('paciente')
    else:
        paciente = get_object_or_404(Paciente, pk=pk)
        form = PacienteForm(request.POST or None, instance=paciente)

    return render(request, plantilla, {'form': form})


#pdf de dia de atencion
@login_required(None, "", 'login')
def exportarListDiadeAtencion(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_diaatencion.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A3)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consultardiadeatencion = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de dias", styles['Heading1'])
    consultardiadeatencion.append(header)
    headings = ('Dias de atencion')
    alldiadeatencion = [(d.descripcion_dia) for d in Dia_atencion.objects.all()]
    print
    alldiadeatencion

    t = Table([headings] + alldiadeatencion)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultardiadeatencion.append(t)
    doc.build(consultardiadeatencion)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#dia de atencion
def consultardiadeatencion(request):
    buscar = request.GET.get("buscar")
    dia= Dia_atencion.objects.all()

    if buscar:
        dia = Dia_atencion.objects.filter(
            Q(descripcion_dia__icontains=buscar)

        ).distinct()
    return render(request, 'consultardiadeatencion.html', {'diadeatencion': dia})

#pagina de crear o insertar INSERT
def creardiadeatencion(request, plantilla="creardiadeatencion.html"):

    if request.method == "POST":
        form = Dia_atencionForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('diadeatencion')
    else:
        form = Dia_atencionForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificardiadeatencion(request, pk, plantilla="modificardiadeatencion.html"):
    if request.method == "POST":
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)
        if form.is_valid():
            form.save()
        return redirect('diadeatencion')
    else:
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminardiadeatencion(request, pk, plantilla="eliminardiadeatencion.html"):

    if request.method == "POST":
        form = Dia_atencionForm((request.POST or None))
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        if form.is_valid():
            dia_atencion.delete()
            return redirect('diadeatencion')
    else:
        dia_atencion = get_object_or_404(Dia_atencion, pk=pk)
        form = Dia_atencionForm(request.POST or None, instance=dia_atencion)

    return render(request, plantilla, {'form': form})


#pdf de horario
@login_required(None, "", 'login')
def exportarListHorario(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Horarios.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A3)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consultarhorario = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de horario ", styles['Heading1'])
    consultarhorario.append(header)
    headings = ('Hora de entrada', 'Hora de salida')
    allhorario = [(d.hora_inicio,d.hora_fin) for d in Horario_atencion.objects.all()]
    print
    allhorario

    t = Table([headings] + allhorario)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarhorario.append(t)
    doc.build(consultarhorario)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#horario de atenciones
def consultarhorariodeatencion(request):
    buscar = request.GET.get("buscar")
    horario = Horario_atencion.objects.all()

    if buscar:
        horario = Horario_atencion.objects.filter(
            Q(hora_inicio__icontains=buscar) |
            Q(hora_fin__icontains=buscar)

        ).distinct()
    return render(request, 'consultarhorariodeatencion.html', {'horariodeatencion': horario})

#pagina de crear o insertar INSERT
def crearhorariodeatencion(request, plantilla="crearhorariodeatencion.html"):

    if request.method == "POST":
        form = Horario_atencionForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('horariodeatencion')
    else:
        form = Horario_atencionForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarhorariodeatencion(request, pk, plantilla="modificarhorariodeatencion.html"):
    if request.method == "POST":
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)
        if form.is_valid():
            form.save()
        return redirect('horariodeatencion')
    else:
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)
    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarhorariodeatencion(request, pk, plantilla="eliminarhorariodeatencion.html"):

    if request.method == "POST":
        form = Horario_atencionForm((request.POST or None))
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        if form.is_valid():
            horario_atencion.delete()
            return redirect('horariodeatencion')
    else:
        horario_atencion = get_object_or_404(Horario_atencion, pk=pk)
        form = Horario_atencionForm(request.POST or None, instance=horario_atencion)

    return render(request, plantilla, {'form': form})


#pdf de antecedente
@login_required(None, "", 'login')
def exportarListAntecedentes(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_antecedentes.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A3)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consultarantecedentes = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de antecedentes ", styles['Heading1'])
    consultarantecedentes.append(header)
    headings = ('Descripcion')
    allantecedente = [(d.descripcion) for d in Antecedente.objects.all()]
    print
    allantecedente

    t = Table([headings] + allantecedente)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarantecedentes.append(t)
    doc.build(consultarantecedentes)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#antecedentes
def consultarantecedentes(request):
    buscar = request.GET.get("buscar")
    antecedentes = Antecedente.objects.all()

    if buscar:
        antecedentes = Antecedente.objects.filter(
            Q(descripcion__icontains=buscar)

        ).distinct()
    return render(request, 'consultarantecedentes.html', {'antecedente':antecedentes})

#pagina de crear o insertar INSERT
def crearantecedentes(request, plantilla="crearantecedentes.html"):
    if request.method == "POST":
        form = AntecedenteForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('antecedentes')
    else:
        form = AntecedenteForm

    return render(request, plantilla, {'form': form})
#pagina de modificar

def modificarantecedentes(request, pk, plantilla="modificarantecedentes.html"):
    if request.method == "POST":
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)
        if form.is_valid():
            form.save()
        return redirect('antecedentes')
    else:
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)
    return render(request, plantilla, {'form': form})
#pagina de eliminar

def eliminarantecedentes(request, pk, plantilla="eliminarantecedentes.html"):

    if request.method == "POST":
        form = AntecedenteForm((request.POST or None))
        antecedente = get_object_or_404(Antecedente, pk=pk)
        if form.is_valid():
            antecedente.delete()
            return redirect('antecedentes')
    else:
        antecedente = get_object_or_404(Antecedente, pk=pk)
        form = AntecedenteForm(request.POST or None, instance=antecedente)
    return render(request, plantilla, {'form': form})


#pdf de examen
@login_required(None, "", 'login')
def exportarListExamen(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_examen.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A3)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    consultarexamen = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de examenes ", styles['Heading1'])
    consultarexamen.append(header)
    headings = ('Examenes')
    allexamen = [(d.nombre_examen) for d in Examen.objects.all()]
    print
    allexamen

    t = Table([headings] + allexamen)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarexamen.append(t)
    doc.build(consultarexamen)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#examenes
def consultarexamen(request):
    buscar = request.GET.get("buscar")
    examen = Examen.objects.all()
    if buscar:
        examen = Examen.objects.filter(
            Q(nombre_examen__icontains=buscar)

        ).distinct()
    return render(request, 'consultarexamen.html', {'examen':examen})

#pagina de crear o insertar INSERT
def crearexamen(request, plantilla="crearexamen.html"):

    if request.method == "POST":
        form = ExamenForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('examen')
    else:
        form = ExamenForm
    return render(request, plantilla, {'form': form})
#pagina de modificar

def modificarexamen(request, pk, plantilla="modificarexamen.html"):
    if request.method == "POST":
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)
        if form.is_valid():
            form.save()
        return redirect('examen')
    else:
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)
    return render(request, plantilla, {'form': form})
#pagina de eliminar

def eliminarexamen(request, pk, plantilla="eliminarexamen.html"):

    if request.method == "POST":
        form = ExamenForm((request.POST or None))
        examen = get_object_or_404(Examen, pk=pk)
        if form.is_valid():
            examen.delete()
            return redirect('examen')
    else:
        examen = get_object_or_404(Examen, pk=pk)
        form = ExamenForm(request.POST or None, instance=examen)

    return render(request, plantilla, {'form': form})



#pdf de consulta
@login_required(None, "", 'login')
def exportarListConsultas(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Consulta.pdf"'

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

    consultarconsulta = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Tratamiento", styles['Heading1'])
    consultarconsulta.append(header)
    headings = ('Fecha de consulta','Motivo de la consulta','Medico', 'Paciente')
    allconsulta= [(d.fecha_consulta,d.motivoconsulta, d.medico, d.paciente) for d in Consulta.objects.all()]
    print
    allconsulta

    t = Table([headings] + allconsulta)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarconsulta.append(t)
    doc.build(consultarconsulta)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#consulta
def consultarconsulta(request):
    buscar = request.GET.get("buscar")
    consulta = Consulta.objects.all()

    if buscar:
        consulta = Consulta.objects.filter(
            Q(fecha_consulta__icontains=buscar) |
            Q(motivoconsulta__icontains=buscar) |
            Q(nombre__icontains=buscar) |
            Q(paciente__icontains=buscar)

        ).distinct()
    return render(request, 'consultarconsulta.html',{'consulta':consulta})

#pagina de crear o insertar INSERT
def crearconsulta(request, plantilla="crearconsulta.html"):
    if request.method == "POST":
        form = ConsultaForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('consulta')
    else:
        form = ConsultaForm
    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarconsulta(request, pk, plantilla="modificarconsulta.html"):
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)
        if form.is_valid():
            form.save()
        return redirect('consulta')
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)
    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarconsulta(request, pk, plantilla="eliminarconsulta.html"):

    if request.method == "POST":
        form = ConsultaForm((request.POST or None))
        consulta = get_object_or_404(Consulta, pk=pk)
        if form.is_valid():
            consulta.delete()
            return redirect('consulta')
    else:
        consulta = get_object_or_404(Consulta, pk=pk)
        form = ConsultaForm(request.POST or None, instance=consulta)

    return render(request, plantilla, {'form': form})

#examen de consulta
def consultarexamenconsulta(request, plantilla="consultarexamenconsulta.html"):
    examenconsulta = Examen_consulta.objects.all()
    data = {
        'examenconsulta':examenconsulta
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def crearexamenconsulta(request, plantilla="crearexamenconsulta.html"):

    if request.method == "POST":
        form = Examen_consultaForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('examenconsulta')
    else:
        form = Examen_consultaForm

    return render(request, plantilla, {'form': form})
#pagina de modificar
def modificarexamenconsulta(request, pk, plantilla="modificarexamenconsulta.html"):
    if request.method == "POST":
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)
        if form.is_valid():
            form.save()
        return redirect('examenconsulta')
    else:
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)



    return render(request, plantilla, {'form': form})
#pagina de eliminar
def eliminarexamenconsulta(request, pk, plantilla="eliminarexamenconsulta.html"):

    if request.method == "POST":
        form = Examen_consultaForm((request.POST or None))
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        if form.is_valid():
            examenconsulta.delete()
            return redirect('examenconsulta')
    else:
        examenconsulta = get_object_or_404(Examen_consulta, pk=pk)
        form = Examen_consultaForm(request.POST or None, instance=examenconsulta)

    return render(request, plantilla, {'form': form})


#pdf de consulta
@login_required(None, "", 'login')
def exportarListHorarioMedico(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_horario.pdf"'

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

    consultarhorario = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de horario", styles['Heading1'])
    consultarhorario.append(header)
    headings = ('Medico','Dia de atencion','Horario de atencion')
    allhorario= [(d.medico,d.dia_atencion, d.horario_atencion) for d in Horario_medico.objects.all()]
    print
    allhorario

    t = Table([headings] + allhorario)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarhorario.append(t)
    doc.build(consultarhorario)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#horario del medico
def consultarhorariomedico(request, plantilla="consultarhorariomedico.html"):
    horariomedico = Horario_medico.objects.all()
    data = {
        'horariomedico':horariomedico
    }
    return render(request, plantilla, data)

#pagina de crear o insertar INSERT
def crearhorariomedico(request, plantilla="crearhorariomedico.html"):

    if request.method == "POST":
        form = Horario_medicoForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('horariomedico')
    else:
        form = Horario_medicoForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarhorariomedico(request, pk, plantilla="modificarhorariomedico.html"):
    if request.method == "POST":
        horariomedico = get_object_or_404(Horario_medico, pk=pk)
        form = Horario_medicoForm(request.POST or None, instance=horariomedico)
        if form.is_valid():
            form.save()
        return redirect('horariomedico')
    else:
        horariomedico = get_object_or_404(Horario_medico, pk=pk)
        form = Horario_medicoForm(request.POST or None, instance=horariomedico)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarhorariomedico(request, pk, plantilla="eliminarhorariomedico.html"):
    if request.method == "POST":
        form = Horario_medicoForm((request.POST or None))
        horariomedico = get_object_or_404(Horario_medico, pk=pk)
        if form.is_valid():
            horariomedico.delete()
            return redirect('horariomedico')
    else:
        horariomedico = get_object_or_404(Horario_medico, pk=pk)
        form = Horario_medicoForm(request.POST or None, instance=horariomedico)
    return render(request, plantilla, {'form': form})

#pdf de reservaciones
@login_required(None, "", 'login')
def exportarListReservaciones(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Reservaciones.pdf"'

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

    consultarreservaciones = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Reservaciones ", styles['Heading1'])
    consultarreservaciones.append(header)
    headings = ('Fecha de Ingreso','Fecha de Reservacion','Medico', 'Paciente', 'Horario')
    allreservaciones = [(d.fecha_ingreso,d.fecha_reservacion, d.medico, d.pacientes, d.horario) for d in Reservaciones.objects.all()]
    print
    allreservaciones

    t = Table([headings] + allreservaciones)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultarreservaciones.append(t)
    doc.build(consultarreservaciones)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#reservaciones
def consultarreservaciones(request):
    buscar = request.GET.get("buscar")
    reservaciones = Reservaciones.objects.all()

    if buscar:
        reservaciones = Reservaciones.objects.filter(
            Q(fecha_ingreso__contains=buscar) |
            Q(fecha_reservacion__contains=buscar) |
            Q(estado_reservacion__contains=buscar) |
            Q(horario__contains=buscar) |
            Q(pacientes__contains=buscar) |
            Q(medico__contains=buscar)

        ).distinct()

    return render(request, 'consultarreservaciones.html', {'reservaciones': reservaciones})

#pagina de crear o insertar INSERT
def crearreservaciones(request, plantilla="crearreservaciones.html"):

    if request.method == "POST":
        form = ReservacionesForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('reservaciones')
    else:
        form = ReservacionesForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificarreservaciones(request, pk, plantilla="modificarreservaciones.html"):
    if request.method == "POST":
        reservaciones = get_object_or_404(Reservaciones, pk=pk)
        form = ReservacionesForm(request.POST or None, instance=reservaciones)
        if form.is_valid():
            form.save()
        return redirect('reservaciones')
    else:
        reservaciones = get_object_or_404(Reservaciones, pk=pk)
        form = ReservacionesForm(request.POST or None, instance=reservaciones)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminarreservaciones(request, pk, plantilla="eliminarreservaciones.html"):

    if request.method == "POST":
        form = ReservacionesForm((request.POST or None))
        reservaciones = get_object_or_404(Reservaciones, pk=pk)
        if form.is_valid():
            reservaciones.delete()
            return redirect('reservaciones')
    else:
        reservaciones = get_object_or_404(Reservaciones, pk=pk)
        form = ReservacionesForm(request.POST or None, instance=reservaciones)

    return render(request, plantilla, {'form': form})


#pdf de tratamiento
@login_required(None, "", 'login')
def exportarListTratamiento(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_Tratamiento.pdf"'

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

    consultartratamiento = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Listado de Tratamiento", styles['Heading1'])
    consultartratamiento.append(header)
    headings = ('Fecha de tratamiento','Diagnostico','Medico', 'Procedimiento', 'Consulta')
    alltratamiento = [(d.fecha_tratamiento,d.diagnostico, d.medico, d.procedimiento, d.consulta) for d in Tratamiento.objects.all()]
    print
    alltratamiento

    t = Table([headings] + alltratamiento)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    consultartratamiento.append(t)
    doc.build(consultartratamiento)
    response.write(buffer.getvalue())
    buffer.close()
    return response

#examen de consulta
def consultartratamiento(request, plantilla="consultartratamiento.html"):
    tratamiento = Tratamiento.objects.all()
    data = {
        'tratamiento':tratamiento
    }
    return render(request, plantilla, data)

#pagina de crear o insertar INSERT
def creartratamiento(request, plantilla="creartratamiento.html"):

    if request.method == "POST":
        form = TratamientoForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('tratamiento')
    else:
        form = TratamientoForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificartratamiento(request, pk, plantilla="modificartratamiento.html"):
    if request.method == "POST":
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        form = TratamientoForm(request.POST or None, instance=tratamiento)
        if form.is_valid():
            form.save()
        return redirect('tratamiento')
    else:
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        form = TratamientoForm(request.POST or None, instance=tratamiento)



    return render(request, plantilla, {'form': form})

#pagina de eliminar
def eliminartratamiento(request, pk, plantilla="eliminartratamiento.html"):

    if request.method == "POST":
        form = TratamientoForm((request.POST or None))
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        if form.is_valid():
            tratamiento.delete()
            return redirect('tratamiento')
    else:
        tratamiento = get_object_or_404(Tratamiento, pk=pk)
        form = TratamientoForm(request.POST or None, instance=tratamiento)

    return render(request, plantilla, {'form': form})