from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializer import PagamentSerializer
from .models import Pagaments
from carreto.models import Carreto
from comandes.models import Ordre


# Pagar una comanda
@api_view(["POST"])
def pagar(request, id):
    # Comprovar que la ordre existeixi
    try:
        ordre = Ordre.objects.get(id=id)
    except Ordre.DoesNotExist:
        return Response(
            {"Error": "Aquesta ordre no existeix"}, status=status.HTTP_404_NOT_FOUND
        )

    # Demanar les dades de la tarjeta de crèdit
    numero_tarjeta = request.data.get("numero_tarjeta")
    data_caducitat = request.data.get("data_caducitat")
    ccv = request.data.get("ccv")

    # Si no es proporcionen, tornar un error
    if not numero_tarjeta or not data_caducitat or not ccv:
        return Response(
            {"Error": "Falten dades de la targeta"}, status=status.HTTP_400_BAD_REQUEST
        )

    # Canviar el valor de pagat del carretó a true
    carreto = Carreto.objects.get(id=ordre.carreto_id)
    carreto.pagat = True
    carreto.save()

    # Recuperar els valors
    ordre = Ordre.objects.get(carreto=carreto)
    pagament = Pagaments(ordre=ordre, pagat=True)
    pagament.save()

    pagament_serializer = PagamentSerializer(pagament)
    return Response(pagament_serializer.data, status=status.HTTP_200_OK)


# Consultar estat comanda (esta pagat o no)
@api_view(["GET"])
def estatComanda(request, id):
    try:
        ordre = Ordre.objects.get(id=id)
    except Ordre.DoesNotExist:
        return Response(
            {"Error": "Aquesta ordre no existeix"}, status=status.HTTP_404_NOT_FOUND
        )

    carreto = Carreto.objects.get(id=ordre.carreto_id)
    if carreto.pagat == True:
        return Response({"Aquesta comanda està pagada"}, status=status.HTTP_200_OK)
    else:
        return Response({"La comanda no està pagada"}, status=status.HTTP_200_OK)
