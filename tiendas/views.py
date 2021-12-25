from django.shortcuts import render
from .models import tiendas as Tiendas
from productos.models import Productos

def landing(request):
    tiendas = Tiendas.objects.all()
    productos = Productos.objects.all()

    return render(request, 'tiendas/landing.html', { 'tiendas': tiendas, 'productos': productos })

def tiendas(request):
    return render(request, 'tiendas/tiendas.html', {})
