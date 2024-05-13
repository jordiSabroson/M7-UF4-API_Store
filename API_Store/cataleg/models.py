from django.db import models
from django.utils import timezone
from carreto.models import Carreto

# Create your models here.


class Producte(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    unitats = models.IntegerField()
    estaActiu = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class LlistaProductes(models.Model):
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantitat = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
