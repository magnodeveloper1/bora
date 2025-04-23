from django.db import models

STATUS = [
    ('active', 'Activo'),
    ('inactive', 'Desativado')
]

STATUS_SELECTED = [
    ('rejected', 'Rejeitado'),
    ('accepted', 'Aceite')
]

# Create your models here.
class TipoZona(models.Model):
    descricao = models.CharField(
        max_length=255,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    def __str__(self):
        return self.descricao
    
class TipoLazer(models.Model):
    descricao = models.CharField(
        max_length=255,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    def __str__(self):
        return self.descricao
    
class TipoEspaco(models.Model):
    descricao = models.CharField(
        max_length=255,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    def __str__(self):
        return self.descricao
    
class Zona(models.Model):

    tipo_de_zona = models.ForeignKey(
        TipoZona,
        on_delete=models.CASCADE
    )

    descricao = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.descricao
    
class Espaco(models.Model):

    tipo_de_espaco = models.ForeignKey(
        TipoEspaco,
        on_delete=models.CASCADE
    )

    zona = models.ForeignKey(
        Zona,
        on_delete=models.CASCADE,
    )

    descricao = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.descricao

class Viagem(models.Model):

    created_at = models.DateField(
        auto_now_add=True
    )

    data_de_viagem = models.DateField(
        null=False,
    )

    tempo_a_fazer = models.IntegerField(
        null=False
    ) # medido em dias

    data_regresso = models.DateField(
        null=False,
    )

    status_ative = models.CharField(
        max_length=30,
        choices=STATUS,
    )

    status_selected = models.CharField(
        max_length=30,
        choices=STATUS_SELECTED,
    )

class Lazer(models.Model):

    descricao = models.CharField(
        max_length=200
    )

    preco = models.FloatField(null=False)

    tempo = models.IntegerField(
        null=True
    ) # em minutos

    tipo_de_lazer = models.ForeignKey(
        TipoLazer,
        on_delete=models.CASCADE,
        null=False,
    )

    espaco = models.ForeignKey(
        Espaco,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.descricao

class Steps(models.Model): # Cada lugar projectado para a viagem
    descricao = models.CharField(
        max_length=200
    )

    data_hora_inicio = models.DateTimeField(null=False)
    data_hora_fim = models.DateTimeField(null=False)

    orcamento = models.FloatField(null=False)

    lazer1 = models.ForeignKey(
        Lazer,
        on_delete=models.CASCADE,
        related_name='Lazer_1'
    )

    lazer2 = models.ForeignKey(
        Lazer,
        on_delete=models.CASCADE,
        related_name='Lazer_2'
    )

    lazer3 = models.ForeignKey(
        Lazer,
        on_delete=models.CASCADE,
        related_name='Lazer_3'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateField(
        auto_now=True,
    )

    viagem = models.ForeignKey(
        Viagem,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.descricao