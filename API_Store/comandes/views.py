from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import OrdreSerializer
from .models import Ordre
from clients.serializer import ClientSerializer
from clients.models import Client
from carreto.models import Carreto
from carreto.serializer import CarretoSerializer


# Mostrar historial de comandes
@api_view(["GET"])
def historial(request):
    listaComandes = Ordre.objects.all()
    data_serializer = OrdreSerializer(listaComandes, many=True)
    return Response({"data": data_serializer.data})


# Mostrar historial de comandes per un client concret
@api_view(["GET"])
def historialClient(request, pk):
    try:
        client = Client.objects.get(id=pk)
    except Client.DoesNotExist:
        return Response(status=404)

    # Filtrar los carretones que pertenecen al cliente
    carretons = Carreto.objects.filter(client=client)
    # Obtener todas las órdenes relacionadas con los carretones del cliente
    ordres = Ordre.objects.filter(carreto__in=carretons)
    # Serializar las órdenes
    data_serializer = OrdreSerializer(ordres, many=True)

    return Response({"data": data_serializer.data})


# Mostrar historial de comandes no finalitzades
@api_view(["GET"])
def historialNoFin(request):
    try:
        carretons = Carreto.objects.filter(pagat=False)
    except Carreto.DoesNotExist:
        return Response(status=404)

    ordres = Ordre.objects.filter(carreto__in=carretons)
    data_serializer = OrdreSerializer(ordres, many=True)

    return Response({"data": data_serializer.data})
