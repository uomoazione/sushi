from django.urls import path
from menu.views import (
    CategoriaDiCiboListView,
    CategoriaDiCiboDetailView,
    CategoriaDiCiboCreateView,
    CategoriaDiCiboUpdateView,
    CategoriaDiCiboDeleteView,
)

app_name = "menu"
urlpatterns = [
    path("categorie/", CategoriaDiCiboListView.as_view(), name="lista_categorie"),
    path(
        "categoria/<int:pk>/",
        CategoriaDiCiboDetailView.as_view(),
        name="dettaglio_categoria",
    ),
    path(
        "categoria/nuova/",
        CategoriaDiCiboCreateView.as_view(),
        name="nuova_categoria",
    ),
    path(
        "categoria/<int:pk>/aggiorna/",
        CategoriaDiCiboUpdateView.as_view(),
        name="modifica_categoria",
    ),
    path(
        "categoria/<int:pk>/elimina/",
        CategoriaDiCiboDeleteView.as_view(),
        name="elimina_categoria",
    ),
]
