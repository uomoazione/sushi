from django.db import models

# Create your models here.
class CategoriaDiCibo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Pietanza(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    categoria = models.ForeignKey(
        CategoriaDiCibo, on_delete=models.PROTECT
    )  # se uno prova a cancellare la categoria primi
    # prima deve spostare tutte le pietanze
