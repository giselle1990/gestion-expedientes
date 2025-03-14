from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Expediente
from .forms import ExpedienteForm

def lista_expedientes(request):
    expedientes = Expediente.objects.all()
    return render(request, 'estudio/inicio.html', {'expedientes': expedientes})

def agregar_expediente(request):
    if request.method == 'POST':
        form = ExpedienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_expedientes')
    else:
        form = ExpedienteForm()
    return render(request, 'estudio/agregar_expediente.html', {'form': form})

def inicio(request):
    expedientes = Expediente.obtener_todos_expedientes()
    return render(request, 'estudio/inicio.html', {'expedientes': expedientes})

def eliminar_todos_expedientes(request):
    Expediente.objects.all().delete()
    return redirect('lista_expedientes')
