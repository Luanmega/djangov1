from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('tiendas', views.tiendas, name='tiendas'),
    path('add_tienda', views.add_tienda, name='add_tienda'),
]