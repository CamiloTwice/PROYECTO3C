from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Pedido
from .forms import ProductoForm, PedidoForm

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/list.html', {'productos': productos})

def pedido_list(request):
    pedidos = Pedido.objects.all().order_by('-fecha_pedido')
    return render(request, 'productos/list.html', {'pedidos': pedidos})

def pedido_create(request):
    if request.method == 'POST':
        producto = request.POST.get('producto')
        precio = request.POST.get('precio')
        cantidad = request.POST.get('cantidad')
        
        pedido = Pedido(
            producto=producto,
            precio=precio,
            cantidad=cantidad
        )
        pedido.save()
        
        messages.success(request, 'Pedido creado exitosamente!')
        return redirect('pedido_list')
        
    return render(request, 'productos/create.html')