from rest_framework import serializers
from .models import Ordre
from clients.serializer import ClientSerializer


class OrdreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordre
        fields = "_all_"
