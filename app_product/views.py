from django.shortcuts import render
from app_product.serializer import ProductListSerializer, ProductcreateSerializer
from app_product.models import Product
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class ListAllProductApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer



class CreateProductApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductcreateSerializer


class ProductRUBApiView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductcreateSerializer
    lookup_field = "id"