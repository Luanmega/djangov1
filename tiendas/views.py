from django.shortcuts import render

def landing(request):
    return render(request, 'tiendas/landing.html', {})

def tiendas(request):
    return render(request, 'tiendas/tiendas.html', {})
