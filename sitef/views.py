from django.views.generic import TemplateView

# Views
class InicioView(TemplateView):
    template_name = "index.html"