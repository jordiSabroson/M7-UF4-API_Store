from django.db import models
from clients.models import Client
from django.utils import timezone


# Create your models here.
class Carreto(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
