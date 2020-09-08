from django.contrib import admin
from django.urls import path, include
from medicos import views
urlpatterns = [
    path('medicos/', views.medico, name="medicos"),
    path('crearmedicos/', views.crearmedicos, name="crearmedicos"),
    path('modificarmedicos/<int:pk>', views.modificarmedicos, name="modificarmedicos"),
    path('eliminarmedicos/<int:pk>', views.eliminarmedicos, name="eliminarmedicos"),

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

    #url de dia de atencion
    path('diadeatencion/', views.consultardiadeatencion, name="diadeatencion"),
    path('creardiadeatencion/', views.creardiadeatencion, name="creardiadeatencion"),
    path('modificardiadeatencion/<int:pk>', views.modificardiadeatencion, name="modificardiadeatencion"),
    path('eliminardiadeatencion/<int:pk>', views.eliminardiadeatencion, name="eliminardiadeatencion"),

    #url de horario de atencion
    path('horariodeatencion/', views.consultarhorariodeatencion, name="horariodeatencion"),
    path('crearhorariodeatencion/', views.crearhorariodeatencion, name="crearhorariodeatencion"),
    path('modificarhorariodeatencion/<int:pk>', views.modificarhorariodeatencion, name="modificarhorariodeatencion"),
    path('eliminarhorariodeatencion/<int:pk>', views.eliminarhorariodeatencion, name="eliminarhorariodeatencion"),

    #url de antecedente
    path('antecedentes/', views.consultarantecedentes, name="antecedentes"),
    path('crearantecedentes/', views.crearantecedentes, name="crearantecedentes"),
    path('modificarantecedentes/<int:pk>', views.modificarantecedentes, name="modificarantecedentes"),
    path('eliminarantecedentes/<int:pk>', views.eliminarantecedentes, name="eliminarantecedentes"),

    #url de examenes
    path('examen/', views.consultarexamen, name="examen"),
    path('crearexamen/', views.crearexamen, name="crearexamen"),
    path('modificarexamen/<int:pk>', views.modificarexamen, name="modificarexamen"),
    path('eliminarexamen/<int:pk>', views.eliminarexamen, name="eliminarexamen"),

    # url de consulta
    path('consulta/', views.consultarconsulta, name="consulta"),
    path('crearconsulta/', views.crearconsulta, name="crearconsulta"),
    path('modificarconsulta/<int:pk>', views.modificarconsulta, name="modificarconsulta"),
    path('eliminarconsulta/<int:pk>', views.eliminarconsulta, name="eliminarconsulta"),
]