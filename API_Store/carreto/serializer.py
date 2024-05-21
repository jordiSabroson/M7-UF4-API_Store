from rest_framework import serializers
from .models import Carreto
from comandes.models import Ordre
from cataleg.models import LlistaProductes
from cataleg.serializer import ProducteSerializer


class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreto
        fields = "__all__"


class LlistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LlistaProductes
        fields = "__all__"


class LlistaProductesProducteSerializer(serializers.ModelSerializer):
    product = ProducteSerializer()

    class Meta:
        model = LlistaProductes
        fields = "_all_"


class OrdreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordre
        fields = "__all__"
