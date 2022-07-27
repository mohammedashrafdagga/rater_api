from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Product, Rater


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'descriptions',)


class RaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rater
        fields = ('id', 'user', 'product', 'starts',)
