from django.shortcuts import render
from django.views.generic import ListView, DetailView
from menu.models import CategoriaDiCibo

# Create your views here.
class CategoriaDiCiboListView(ListView):
    model = CategoriaDiCibo


class CategoriaDiCiboDetailView(DetailView):
    model = CategoriaDiCibo
