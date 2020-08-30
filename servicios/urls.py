from django.contrib import admin
from django.urls import path, include
from servicios import views
urlpatterns = [
    #path('medicos/',views.medico, name="medicos"),
    path('crearservicios/', views.crearservicios, name="crearservicios"),
]