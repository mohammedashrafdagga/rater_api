from django.shortcuts import render
from .serializer import ProductSerializer, RaterSerializer
from .models import Product, Rater
from rest_framework import viewsets
# Create your views here.
# add Serializer View


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RaterViewSet(viewsets.ModelViewSet):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer
