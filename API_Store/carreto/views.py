from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CarretoSerializer, LlistaSerializer
from cataleg.models import LlistaProductes


# Crear carretó
@api_view(["POST"])
def nouCarreto(request):
    serializer = CarretoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Afegir productes al carretó
@api_view(["POST"])
def afegirProductes(request):
    serializer = LlistaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Eliminar productes del carretó
@api_view(["DELETE"])
def eliminarProducte(request, id):
    try:
        producte = LlistaProductes.objects.get(id=id)
    except LlistaProductes.DoesNotExist:
        return Response(status=404)
    serializer = LlistaProductes(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
