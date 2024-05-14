from django.urls import path
from . import views

urlpatterns = [
    path("nouCarreto/", views.nouCarreto, name="nouCarreto"),
    path("afegirProducte/", views.afegirProductes, name="afegirProducte"),
    path("eliminarProducte/<str:id>", views.eliminarProducte, name="eliminarProducte"),
]
