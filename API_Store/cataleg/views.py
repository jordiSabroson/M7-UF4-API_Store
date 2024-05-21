from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProducteSerializer
from .models import Producte

# Create your views here.


# Veure tots els productes
@api_view(["GET"])
def productes(request):
    listaProductes = Producte.objects.all()
    listaProductes = listaProductes.filter(estaActiu=True)
    data_serializer = ProducteSerializer(listaProductes, many=True)
    return Response({"data": data_serializer.data})


# Veure informació detallada d'un producte
@api_view(["GET"])
def producte(request, pk):
    producte = Producte.objects.get(id=pk)
    if producte.estaActiu == False:
        return Response({"Error": "No existe el producto"}, status=400)
    data_serializer = ProducteSerializer(producte, many=False)
    return Response({"data": data_serializer.data})


# Afegir nous productes
@api_view(["POST"])
def nouProducte(request):
    serializer = ProducteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Actualitzar productes
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


# Actualitzar stock productes
@api_view(["PUT"])
def editaStockProducte(request, pk):
    try:
        producte = Producte.objects.get(id=pk)
        if producte.estaActiu == False:
            return Response({"Error": "No existe el producto"}, status=400)
    except Producte.DoesNotExist:
        return Response(status=404)
    # Obtener la instancia de las unidades del producto
    unitats_instance = producte.unitats

    # Serializar y actualizar solo las unidades
    serializer = ProducteSerializer(producte, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# Eliminar productes a través d'un borrat lògic
@api_view(["DELETE"])
def eliminaProducte(request, pk):
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
