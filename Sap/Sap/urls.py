"""
URL configuration for Sap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path

from Autos.views import detalleAuto, agregarAuto, eliminarAuto, actualizarAuto
from Webapp.views import SelectCar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Bienvenido/', SelectCar, name='inicio'),
    path('Elementos/<int:id>', detalleAuto),
    path('Nueva_vehiculo/', agregarAuto, name='agregar'),
    path('Borrar_Vehiculo/<int:id>', eliminarAuto, name='eliminar'),
    path('Actualizar_Vehiculo/<int:id>', actualizarAuto, name='actualizar'),

]