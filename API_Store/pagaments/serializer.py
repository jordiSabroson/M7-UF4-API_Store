from rest_framework import serializers
from .models import Pagaments


class PagamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagaments
        fields = "__all__"
