from django.contrib import admin
from .models import Pagamento, FaturaRecibo

# Register your models here.
class PagamentoAdmin(admin.ModelAdmin):
    pass

class FaturaReciboAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(FaturaRecibo, FaturaReciboAdmin)