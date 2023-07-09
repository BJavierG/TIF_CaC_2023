from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Producto

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class ProductoBaseView():
    template_name = "productos_app.html"
    model = Producto
    fields = "__all__"
    succes_url = reverse_lazy("productos:all")

class ProductoListView(ProductoBaseView, ListView):

    """
    Muestra todos los productos!!!
    """

class ProductoDetailView(ProductoBaseView, DetailView):

    template_name = "productos_detail.html"

class ProductoCreateView(ProductoBaseView, CreateView):

    template_name = "productos_create.html"
    extra_context = {
        "tipo" : "Crear Producto"
    }
    succes_url = reverse_lazy("productos:all")

class ProductoUpdateView(ProductoBaseView, UpdateView):

    template_name = "productos_create.html"
    extra_context = {
        "tipo" : "Actualizar Producto"
    }
    succes_url = reverse_lazy("productos:all")
    
class ProductoDeleteView(ProductoBaseView, DeleteView):

    template_name = "productos_delete.html"
    extra_context = {
        "tipo" : "Borrar Producto"
    }
    success_url = reverse_lazy("productos:all")