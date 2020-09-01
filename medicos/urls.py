from django.contrib import admin
from django.urls import path, include
from medicos import views
urlpatterns = [
    path('medicos/', views.medico, name="medicos"),
    path('crearmedicos/', views.crearmedicos, name="crearmedicos"),
    path('modificarmedicos/<int:pk>', views.modificarmedicos, name="modificarmedicos"),
    path('eliminarmedicos/<int:pk>', views.eliminarmedicos, name="eliminarmedicos"),

]