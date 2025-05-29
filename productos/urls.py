from django.urls import path
from .views import producto_list, producto_create, pedido_list, pedido_create

urlpatterns = [
    path('productos/list/', producto_list, name='producto_list'),
    path('productos/create/', producto_create, name='producto_create'),
    path('pedidos/list/', pedido_list, name='pedido_list'),
    path('pedidos/create/', pedido_create, name='pedido_create'),
]