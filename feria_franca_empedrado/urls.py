"""
URL configuration for feria_franca_empedrado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import Landing, Contacto, Productos, Registrarse, SobreNosotros, Tienda, Crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Landing.as_view(), name="landing"),
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('productos/', Productos.as_view(), name="productos"),
    path('registrarse/', Registrarse.as_view(), name="registrarse"),
    path('sobrenosotros/', SobreNosotros.as_view(), name="sobre_nosotros"),
    path('tienda/', Tienda.as_view(), name="tienda"),
    path('crud/', Crud.as_view(), name="crud"),
    path('productos_app/', include("feria_app.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

