from django.contrib import admin
from django.urls import path, include
from medicos import views
from .views import medico
urlpatterns = [
    path('medicos/', views.medico, name="medicos"),
    path('crearmedicos/', views.crearmedicos, name="crearmedicos"),
    path('modificarmedicos/<int:pk>', views.modificarmedicos, name="modificarmedicos"),
    path('eliminarmedicos/<int:pk>', views.eliminarmedicos, name="eliminarmedicos"),
    path('exportarListMedicos/', views.exportarListMedicos, name="exportarListMedicos"),

    #url de usuarios
    path('usuario/', views.consultarusuario, name="usuario"),
    path('crearusuario/', views.crearusuario, name="crearusuario"),
    path('modificarusuario/<int:pk>', views.modificarusuario, name="modificarusuario"),
    path('eliminarusuario/<int:pk>', views.eliminarusuario, name="eliminarusuario"),

    #url de paciente
    path('paciente/', views.consultarpaciente, name="paciente"),
    path('crearpaciente/', views.crearpaciente, name="crearpaciente"),
    path('modificarpaciente/<int:pk>', views.modificarpaciente, name="modificarpaciente"),
    path('eliminarpaciente/<int:pk>', views.eliminarpaciente, name="eliminarpaciente"),
    path('exportarListPaciente/', views.exportarListPaciente, name="exportarListPaciente"),

    #url de dia de atencion
    path('diadeatencion/', views.consultardiadeatencion, name="diadeatencion"),
    path('creardiadeatencion/', views.creardiadeatencion, name="creardiadeatencion"),
    path('modificardiadeatencion/<int:pk>', views.modificardiadeatencion, name="modificardiadeatencion"),
    path('eliminardiadeatencion/<int:pk>', views.eliminardiadeatencion, name="eliminardiadeatencion"),
    path('exportarListDiadeAtencion/', views.exportarListDiadeAtencion, name="exportarListDiadeAtencion"),

    #url de horario de atencion
    path('horariodeatencion/', views.consultarhorariodeatencion, name="horariodeatencion"),
    path('crearhorariodeatencion/', views.crearhorariodeatencion, name="crearhorariodeatencion"),
    path('modificarhorariodeatencion/<int:pk>', views.modificarhorariodeatencion, name="modificarhorariodeatencion"),
    path('eliminarhorariodeatencion/<int:pk>', views.eliminarhorariodeatencion, name="eliminarhorariodeatencion"),
    path('exportarListHorario/', views.exportarListHorario, name="exportarListHorario"),

    #url de antecedente
    path('antecedentes/', views.consultarantecedentes, name="antecedentes"),
    path('crearantecedentes/', views.crearantecedentes, name="crearantecedentes"),
    path('modificarantecedentes/<int:pk>', views.modificarantecedentes, name="modificarantecedentes"),
    path('eliminarantecedentes/<int:pk>', views.eliminarantecedentes, name="eliminarantecedentes"),
    path('exportarListAntecedentes/', views.exportarListAntecedentes, name="exportarListAntecedentes"),

    #url de examenes
    path('examen/', views.consultarexamen, name="examen"),
    path('crearexamen/', views.crearexamen, name="crearexamen"),
    path('modificarexamen/<int:pk>', views.modificarexamen, name="modificarexamen"),
    path('eliminarexamen/<int:pk>', views.eliminarexamen, name="eliminarexamen"),
    path('exportarListExamen/', views.exportarListExamen, name="exportarListExamen"),

    # url de consulta
    path('consulta/', views.consultarconsulta, name="consulta"),
    path('crearconsulta/', views.crearconsulta, name="crearconsulta"),
    path('modificarconsulta/<int:pk>', views.modificarconsulta, name="modificarconsulta"),
    path('eliminarconsulta/<int:pk>', views.eliminarconsulta, name="eliminarconsulta"),
    path('exportarListConsultas/', views.exportarListConsultas, name="exportarListConsultas"),

    # url de examenes de consulta
    path('examenconsulta/', views.consultarexamenconsulta, name="examenconsulta"),
    path('crearexamenconsulta/', views.crearexamenconsulta, name="crearexamenconsulta"),
    path('modificarexamenconsulta/<int:pk>', views.modificarexamenconsulta, name="modificarexamenconsulta"),
    path('eliminarexamenconsulta/<int:pk>', views.eliminarexamenconsulta, name="eliminarexamenconsulta"),

    # url de horario del medico
    path('horariomedico/', views.consultarhorariomedico, name="horariomedico"),
    path('crearhorariomedico/', views.crearhorariomedico, name="crearhorariomedico"),
    path('modificarhorariomedico/<int:pk>', views.modificarhorariomedico, name="modificarhorariomedico"),
    path('eliminarhorariomedico/<int:pk>', views.eliminarhorariomedico, name="eliminarhorariomedico"),
    path('exportarListHorarioMedico/', views.exportarListHorarioMedico, name="exportarListHorarioMedico"),

    # url de reservacions
    path('reservaciones/', views.consultarreservaciones, name="reservaciones"),
    path('crearreservaciones/', views.crearreservaciones, name="crearreservaciones"),
    path('modificarreservaciones/<int:pk>', views.modificarreservaciones, name="modificarreservaciones"),
    path('eliminarreservaciones/<int:pk>', views.eliminarreservaciones, name="eliminarreservaciones"),
    path('exportarListReservaciones/', views.exportarListReservaciones, name="exportarListReservaciones"),

    # url de tratamiento
    path('tratamiento/', views.consultartratamiento, name="tratamiento"),
    path('creartratamiento/', views.creartratamiento, name="creartratamiento"),
    path('modificartratamiento/<int:pk>', views.modificartratamiento, name="modificartratamiento"),
    path('eliminartratamiento/<int:pk>', views.eliminartratamiento, name="eliminartratamiento"),
    path('exportarListTratamiento/', views.exportarListTratamiento, name="exportarListTratamiento"),
]