from django.shortcuts import get_object_or_404, render
from .models import tiendas as Tiendas
from productos.models import Productos
from django.http import HttpResponse
import json

def landing(request):
    tiendas = Tiendas.objects.all()
    productos = Productos.objects.all()

    return render(request, 'tiendas/landing.html', { 'tiendas': tiendas, 'productos': productos })

def tiendas(request):
    return render(request, 'tiendas/tiendas.html', {})

def add_tienda(request):
    print("PRINTO")
    print(request.body)
    # if request is post and ajax 
    # if request.method == "POST":
    tienda = Tiendas()
    if request.method == 'POST':
        jsonResponse = json.loads(request.body.decode('utf-8'))
        tienda.nombre = jsonResponse['nombre']
        tienda.direccion = jsonResponse['direccion']

        tienda.save()
        return HttpResponse("EXITO VIEW")     

    response = HttpResponse(request.body)
    return response
