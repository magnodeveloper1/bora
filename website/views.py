# some_app/views.py
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "home.html"