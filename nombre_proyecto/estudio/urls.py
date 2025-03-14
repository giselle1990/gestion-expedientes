# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_expedientes, name='lista_expedientes'),
    path('agregar/', views.agregar_expediente, name='agregar_expediente'),
    path('eliminar_todos/', views.eliminar_todos_expedientes, name='eliminar_todos_expedientes'),
    # ...existing code...
]
