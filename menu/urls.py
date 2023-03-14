from django.urls import path
from menu.views import CategoriaDiCiboListView, CategoriaDiCiboDetailView

app_name = "menu"
urlpatterns = [
    path("categorie/", CategoriaDiCiboListView.as_view(), name="lista_categorie"),
    path(
        "categoria/<int:pk>/",
        CategoriaDiCiboDetailView.as_view(),
        name="dettaglio_categoria",
    ),
]
