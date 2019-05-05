from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import MyModel


class MyCreateView(CreateView):
    model = MyModel
    fields = ["somefile"]
