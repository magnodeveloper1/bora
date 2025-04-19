from django.contrib import admin
from .models import Cliente, Viajante

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    pass

class ViajanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Viajante, ViajanteAdmin)
admin.site.register(Cliente, ClienteAdmin)