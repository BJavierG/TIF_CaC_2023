from django.views.generic import TemplateView

class Landing(TemplateView):
    template_name = "pantallas/landing_page.html"

class Contacto(TemplateView):
    template_name = "pantallas/contacto.html"

class Productos(TemplateView):
    template_name = "pantallas/productos.html"

class Registrarse(TemplateView):
    template_name = "pantallas/registrarse.html"

class SobreNosotros(TemplateView):
    template_name = "pantallas/sobrenosotros.html"

class Tienda(TemplateView):
    template_name = "pantallas/tienda.html"

class Crud(TemplateView):
    template_name = "pantallas/crud.html"