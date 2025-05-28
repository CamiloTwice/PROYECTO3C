from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/list.html', {'productos': productos})


def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto created successfully!')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/create.html', {'form': form})

def hilos_list(request):
    hilos = Hilos.objects.all()
    return render(request, 'productos/hilos.html')

def hilos_create(request):
    # Aquí puedes agregar la lógica para manejar las tareas de Celery
    return render(request, 'productos/hilos.html')

def celer_list(request):
    # Aquí puedes agregar la lógica para manejar las tareas de Celery
    return render(request, 'productos/celery.html')

def celery_create(request):
    # Aquí puedes agregar la lógica para manejar las tareas de Celery
    return render(request, 'productos/celery.html')