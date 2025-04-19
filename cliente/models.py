from django.db import models
from viagem.models import Viagem

# Create your models here.
class Cliente(models.Model):

    first_name = models.CharField(
        max_length=200,
        null=False
    )

    last_name = models.CharField(
        max_length=200,
        null=False
    )

    bi = models.CharField(
        max_length=15,
        null=True
    )

    phone_number = models.CharField(
        max_length=15,
        null=False,
    )

    created_at = models.DateField(
        auto_now_add=True,
        editable=False,
    )

    updated_at = models.DateField(
        auto_now=True,
        editable=False,
    )

    # morada de zona

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Viajante(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        null=False,
    )

    viagem = models.ForeignKey(
        Viagem,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

