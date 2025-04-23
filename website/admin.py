from django.contrib import admin
from .models import Contacto, SobreNos

# Register your models here.
class SobreNosAdmin(admin.ModelAdmin):
    pass

class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(SobreNos, SobreNosAdmin)
admin.site.register(Contacto, ContactoAdmin)