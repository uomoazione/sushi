from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from menu.models import CategoriaDiCibo
from django.urls import reverse_lazy


# Create your views here.
class CategoriaDiCiboListView(ListView):
    model = CategoriaDiCibo


class CategoriaDiCiboDetailView(DetailView):
    model = CategoriaDiCibo


class CategoriaDiCiboCreateView(CreateView):
    model = CategoriaDiCibo
    fields = ("name", "description")

    success_url = reverse_lazy("menu:lista_categorie")


class CategoriaDiCiboUpdateView(UpdateView):
    model = CategoriaDiCibo
    fields = ("name", "description")

    success_url = reverse_lazy("menu:lista_categorie")


class CategoriaDiCiboDeleteView(DeleteView):
    model = CategoriaDiCibo
    success_url = reverse_lazy("menu:lista_categorie")
