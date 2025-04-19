from django.db import models
from cliente.models import Cliente
from viagem.models import Viagem

# Create your models here.
class Pagamento(models.Model):
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    viagem = models.ForeignKey(
        Viagem,
        on_delete=models.CASCADE
    )

    valor_a_pagar = models.FloatField(null = False)

    iva = models.FloatField(null = False)

    valor_pago = models.FloatField(null = False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

class FaturaRecibo(models.Model):

    pagamento = models.ForeignKey(
        Pagamento,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )