from django.db import models
from comandes.models import Ordre
from django.utils import timezone

# Create your models here.


class Pagaments(models.Model):
    ordre = models.OneToOneField(Ordre, on_delete=models.CASCADE)
    pagat = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
