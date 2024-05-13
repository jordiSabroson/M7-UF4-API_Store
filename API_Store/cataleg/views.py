from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProducteSerializer
from .models import Producte

# Create your views here.


@api_view(["GET"])
def productes(request):
    listaProductes = Producte.objects.all()
    listaProductes = listaProductes.filter(estaActiu=True)
    data_serializer = ProducteSerializer(listaProductes, many=True)
    return Response({"data": data_serializer.data})


@api_view(["GET"])
def producte(request, pk):
    producte = Producte.objects.get(id=pk)
    if producte.estaActiu == False:
        return Response({"Error": "No existe el producto"}, status=400)
    data_serializer = ProducteSerializer(producte, many=False)
    return Response({"data": data_serializer.data})


@api_view(["POST"])
def nouProducte(request):
    serializer = ProducteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def editaProducte(request, pk):
    try:
        producte = Producte.objects.get(id=pk)
        if producte.estaActiu == False:
            return Response({"Error": "No existe el producto"}, status=400)
    except Producte.DoesNotExist:
        return Response(status=404)
    serializer = ProducteSerializer(producte, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def eliminaProducte(request, pk):
    # producte = Producte.objects.get(id=pk)
    # serializer= ProducteSerializer(producte, data=request.data ,partial=True)
    # if serializer.is_valid():
    #     producte.delete()
    #     return Response(serializer.data, status=201)
    # return Response(serializer.errors, status=400)
    try:
        producte = Producte.objects.get(id=pk)
        if producte.estaActiu == False:
            return Response({"Error": "No existe el producto"}, status=400)
    except Producte.DoesNotExist:
        return Response(status=404)
    serializer = ProducteSerializer(producte, data=request.data, partial=True)
    if serializer.is_valid():
        producte.estaActiu = False
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
