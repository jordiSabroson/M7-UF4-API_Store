from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import (
    CarretoSerializer,
    LlistaSerializer,
    LlistaProductesProducteSerializer,
)
from cataleg.models import LlistaProductes
from .models import Carreto
from comandes.models import Ordre
from django.shortcuts import get_object_or_404


# Crear carretó
@api_view(["POST"])
def nouCarreto(request):
    serializer = CarretoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Afegir productes al carretó
@api_view(["POST"])
def afegirProductes(request):
    quantitat = request.data.get("quantitat")
    carreto_id = request.data.get("carreto")
    producte_id = request.data.get("producte")

    # Verificar si el carreto existeix i està actiu
    try:
        carreto = Carreto.objects.get(id=carreto_id)
        if not carreto.estaActiu:
            return Response(
                {"Error": "Aquest carretó està tancat, has de crear un de nou"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except Carreto.DoesNotExist:
        return Response(
            {"Error": "El carretó no existeix"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Crear el producte si el carreto esta actiu
    data = {"quantitat": quantitat, "carreto": carreto_id, "producte": producte_id}

    serializer = LlistaSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Eliminar productes del carretó
@api_view(["DELETE"])
def eliminarProducte(request, id):
    producte = get_object_or_404(LlistaProductes, id=id)

    producte.delete()
    return Response(
        {"message": f"Producte amb id: {id} eliminat"}, status=status.HTTP_200_OK
    )


# Eliminar tot el carretó
@api_view(["DELETE"])
def eliminarCarreto(request, id):
    carreto = get_object_or_404(Carreto, id=id)

    carreto.delete()
    return Response(
        {"message": f"Carreto amb id: {id} eliminat"}, status=status.HTTP_200_OK
    )


# Modificar quantitat d'un producte
@api_view(["PUT"])
def modificarQuantitat(request, id):
    try:
        producte = LlistaProductes.objects.get(id=id)
    except LlistaProductes.DoesNotExist:
        return Response(
            {"Error": "El producte no existeix"}, status=status.HTTP_404_NOT_FOUND
        )
    nova_quantitat = request.data.get("quantitat")

    if nova_quantitat is None:
        return Response(
            {"Error": "No s'ha proporcionat cap quantitat"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    producte.quantitat = nova_quantitat
    producte.save()

    serializer = LlistaSerializer(producte)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Consultar el llistat de productes del carretó
@api_view(["GET"])
def llistatProductesCarreto(request, pk):
    llista = LlistaProductes.objects.get(carreto_id=pk)
    data_serializer = LlistaProductesProducteSerializer(llista, many=True)
    return Response({"data": data_serializer.data})


# Comprar (desactivar el carretó)
@api_view(["DELETE"])
def comprar(request, id):
    try:
        carreto = Carreto.objects.get(id=id)
    except carreto.DoesNotExist:
        return Response(
            {"Error": "El carretó no existeix"}, status=status.HTTP_404_NOT_FOUND
        )
    serializer = CarretoSerializer(carreto, data=request.data, partial=True)
    if serializer.is_valid():
        carreto.estaActiu = False
        serializer.save()

        nova_comanda = Ordre(carreto=carreto)
        nova_comanda.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
