from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('tiendas/<int:pk>/', views.tiendas, name='tiendas'),
    path('add_tienda', views.add_tienda, name='add_tienda'),
    path('delete_tienda/<int:pk>/', views.delete_tienda, name='delete_tienda')
]