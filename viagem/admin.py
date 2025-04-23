from django.contrib import admin
from .models import Viagem, Zona, Espaco, Lazer, Steps, TipoZona, TipoLazer, TipoEspaco

# Register your models here.
class ViagemAdmin(admin.ModelAdmin):
    pass

class ZonaAdmin(admin.ModelAdmin):
    pass

class EspacoAdmin(admin.ModelAdmin):
    pass

class LazerAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco', 'tipo_de_lazer', 'espaco')

class StepsAdmin(admin.ModelAdmin):
    pass

class TipoZonaAdmin(admin.ModelAdmin):
    pass

class TipoLazerAdmin(admin.ModelAdmin):
    pass

class TipoEspacoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Viagem, ViagemAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(Espaco, EspacoAdmin)
admin.site.register(Lazer, LazerAdmin)
admin.site.register(Steps, StepsAdmin )
admin.site.register(TipoZona, TipoZonaAdmin)
admin.site.register(TipoLazer, TipoLazerAdmin)
admin.site.register(TipoEspaco, TipoEspacoAdmin)