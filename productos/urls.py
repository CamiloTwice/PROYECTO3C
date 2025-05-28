from django.urls import path
from .views import producto_list, producto_create

urlpatterns = [
    path('', producto_list, name='producto_list'),  # List view for products
    path('create/', producto_create, name='producto_create'),  # Create view for products
]