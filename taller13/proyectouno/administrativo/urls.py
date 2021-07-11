"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('edificio/<int:id>', views.obtener_edificio, 
            name='obtener_edificio'),
        path('crear/edificio_crear', views.crear_edificio, 
            name='crear_edificio'),
        path('editar_edificio/<int:id>', views.editar_edificio, 
            name='editar_edificio'),
        path('eliminar/edificio_eliminar/<int:id>', views.eliminar_edificio, 
            name='eliminar_edificio'),
        # numeros telefonicos
        path('crear/Departamento/departamento', views.crear_Departamento, 
            name='crear_Departamento'),
        path('editar/Departamento/departamento/<int:id>', views.editar_Departamentoo, 
            name='editar_Departamentoo'),
        path('crear/Departamento/departamento/depart/<int:id>', views.crear_numero_Departamento, 
            name='crear_numero_Departamento'),
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
        
 ]
