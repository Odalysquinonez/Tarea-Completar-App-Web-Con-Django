from django.forms import modelform_factory, ModelForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from Autos.models import Auto


def detalleAuto(request,id):
    Vehiculo = get_object_or_404(Auto, pk=id)
    return render (request, 'Autos/Caracteristicas.html',{'Detalle': Vehiculo})


# AutoForm = modelform_factory(Auto,exclude=[])
#class AutoForm (ModelForm):

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = "__all__"



def agregarAuto (request):
    if request.method == 'POST': #crear objeto
        formaAuto = AutoForm(request.POST) #Formulario lleno
        if formaAuto.is_valid():
            formaAuto.save()
            return redirect ('inicio')
        else: #cuando hay formulario con errores
            return render (request,'autos/agregar.Html',{'formaAuto':formaAuto})

    else: #solicitar el formulario vacio GET
        formaAuto = AutoForm()
        return render(request, 'Autos/agregar.Html', {'formaAuto': formaAuto})


def eliminarAuto(request,id):
    Vehiculo = get_object_or_404(Auto,pk=id)
    if Vehiculo:
        Vehiculo.delete()
    return redirect('inicio')

def actualizarAuto(request,id):
    if request.method == 'POST':
        Vehiculo = get_object_or_404(Auto, pk=id)
        formaAuto = AutoForm(request.POST, instance=Vehiculo)
        if formaAuto.is_valid():
            formaAuto.save()
            return redirect('inicio')

        else: #Se activa cuando is_valid es falso
            return render(request, 'autos/actualizar.html', {'formaAuto': formaAuto})

    else: #Cuando es Get (pido formulario lleno con informacion de la BD hasta ese momento), aqui recien voy a editar primera fase
        Vehiculo = get_object_or_404(Auto, pk=id)
        formaAuto =AutoForm(instance=Vehiculo) #Formulario lleno
        return render(request, 'Autos/actualizar.Html', {'formaAuto': formaAuto})


