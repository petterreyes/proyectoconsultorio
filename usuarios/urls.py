from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from usuarios import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    #url(r'^login/$', views.login, name="login"),
    #url(r'^logout/$', views.logout, name="logout"),

    #usuarios
    path('consultar_usuarios/', views.consultarusuarios, name="consultar_usuarios"),
    path('crear_usuario/', views.crearusuario, name="crear_usuario"),
    path('modificar_usuario/<int:pk>', views.modificarusuario, name="modificar_usuario"),
    path('eliminar_usuario/<int:pk>', views.eliminarusuario, name="eliminar_usuario"),

    #roles
    path('consultar_roles/', views.consultarroles, name="consultar_roles"),
    path('crear_rol/', views.crearrol, name="crear_rol"),
    path('modificar_rol/<int:pk>', views.modificarrol, name="modificar_rol"),
    path('eliminar_rol/<int:pk>', views.eliminarrol, name="eliminar_rol"),

    # roles y usuarios relacionados
    path('consultar_roles_usuarios/', views.consultarrolesusuarios, name="consultar_roles_usuarios"),
    path('crear_rol_usuario/', views.crearrolusuario, name="crear_rol_usuario"),
    path('modificar_rol_usuario/<int:pk>', views.modificarrolusuario, name="modificar_rol_usuario"),
    path('eliminar_rol_usuario/<int:pk>', views.eliminarrolusuario, name="eliminar_rol_usuario"),
]