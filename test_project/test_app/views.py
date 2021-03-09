from django.shortcuts import render
from test_app.serializers import ProductSerializer
from test_app.models import Product
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer