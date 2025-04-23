from django.db import models

# Create your models here.
class SobreNos(models.Model):

    descricao = models.TextField(
        null=False
    )

    activo = models.BooleanField()

    created_at = models.DateField(
        null=False,
        auto_now_add=True
    )

    updated_at = models.DateField(
        auto_now=True
    )

class Contacto(models.Model):

    descricao = models.CharField(
        max_length=100,
        null=False,
    )

    contacto = models.CharField(
        max_length=20,
        null=False,
    )

    activo = models.BooleanField()

    created_at = models.DateField(
        null=False,
        auto_now_add=True
    )

    updated_at = models.DateField(
        auto_now=True
    )

    class Meta:
        unique_together = ('descricao', 'activo') 