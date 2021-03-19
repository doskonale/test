from django.shortcuts import render
from test_app.serializers import ProductSerializer, ProjectSerializer
from test_app.models import Product, Project
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer