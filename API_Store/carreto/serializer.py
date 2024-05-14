from rest_framework import serializers
from .models import Carreto
from cataleg.models import LlistaProductes


class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = "__all__"


class LlistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LlistaProductes
        fields = "__all__"
