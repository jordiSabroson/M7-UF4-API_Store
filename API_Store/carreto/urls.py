from django.urls import path
from . import views

urlpatterns = [
    path("nouCarreto/", views.nouCarreto, name="nouCarreto"),
    path("afegirProducte/", views.afegirProductes, name="afegirProducte"),
    path("eliminarProducte/<str:id>", views.eliminarProducte, name="eliminarProducte"),
    path("eliminarCarreto/<str:id>", views.eliminarCarreto, name="eliminarCarreto"),
    path(
        "modificarQuantitat/<str:id>",
        views.modificarQuantitat,
        name="modificarQuantitat",
    ),
    path(
        "llistatProductesCarreto/<str:pk>",
        views.llistatProductesCarreto,
        name="llistatProductesCarreto",
    ),
    path("comprar/<str:id>", views.comprar, name="comprar"),
]
