from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Agenda
from .forms import AgendaFormulario


def index(request):
   registros = Agenda.objects.all()
   context = {'registros': registros}
   return render(request, 'MiPagina.html', context)


def insertar(request):
   data = {
       'form': AgendaFormulario()
   }

   if request.method == "POST":
       formulario = AgendaFormulario(data=request.POST, files=request.FILES)

       if formulario.is_valid:
           formulario.save()
           data["mensaje"] = "Guardado Correctamente"
       else:
           data["form"] = formulario

   return render(request, 'AñadirRegistro.html', data)


def modificar(request, id):
   registro = get_object_or_404(Agenda, ID=id)

   data = {
       'form': AgendaFormulario(instance=registro)
   }

   if request.method == "POST":
       formulario = AgendaFormulario(data=request.POST, files=request.FILES, instance=registro)

       if formulario.is_valid:
           formulario.save()
           return redirect(to='index')
       else:
           data["form"] = formulario

   return render(request, 'ModificarAgenda.html', data)


def eliminar(request, id):
   registro = get_object_or_404(Agenda, ID=id)
   registro.delete()
   return redirect(to='index')