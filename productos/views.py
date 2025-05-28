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