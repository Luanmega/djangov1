from django.shortcuts import get_object_or_404, render, redirect
from .models import tiendas as Tiendas
from productos.models import Productos
from django.http import HttpResponse
import json

#Use request.body when application/json
#Use request.post when not applicacion/json

def landing(request):
    tiendas = Tiendas.objects.all()
    productos = Productos.objects.all()

    return render(request, 'tiendas/landing.html', { 'tiendas': tiendas, 'productos': productos })

def tiendas(request, pk):
    if pk != 0:
        tienda = get_object_or_404(Tiendas, pk=pk)
        return render(request, 'tiendas/tiendas.html', {'tienda' : tienda})
    
    return render(request, 'tiendas/tiendas.html', {})

def add_tienda(request):
    # if request is post and ajax 
    # if request.method == "POST":
    if request.body:
        jsonResponse = json.loads(request.body.decode('utf-8'))
        if jsonResponse['id'] != 0:
            tienda = Tiendas()
            tienda = get_object_or_404(Tiendas, pk=jsonResponse['id'])
        else:
            tienda = Tiendas()

        if request.method == 'POST':
            tienda.nombre = jsonResponse['nombre']
            tienda.direccion = jsonResponse['direccion']

            tienda.save()

            return redirect('landing')

    return redirect('tiendas')

def delete_tienda(request, pk):
    tienda = Tiendas.objects.get(id=pk)
    tienda.delete()

    return redirect("landing")

