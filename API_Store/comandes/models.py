from django.db import models
from carreto.models import Carreto
from django.utils import timezone


# Create your models here.
class Ordre(models.Model):
    carreto = models.OneToOneField(Carreto, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
