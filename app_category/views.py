from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView,
CreateAPIView, RetrieveUpdateDestroyAPIView)
from app_category.models import Category, SubCategory
from app_category.serializer import (CategoryListRUDSerializer, 
CategoryCreateSerializer, SubCategoryListSerializer, SubCategoryCreateSerializer)
from app_product.filters import SearchFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status

class CategoryAllListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRUDSerializer
    filter_backends = [SearchFilter]

    # @method_decorator(cache_page(10))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)



class ListOneCategoryApiView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = CategoryListRUDSerializer

    def get(self, request, id):
        category = Category.objects.filter(id=id)
        serializer = CategoryListRUDSerializer(category, many=True)
        return Response(serializer.data)
    





class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAdminUser, ]

    def create(self, request, *args, **kwargs):
        # Проверяем, что изображение передано в запросе
        if 'image' not in request.data:
            return Response({"error": "Image is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Создаем экземпляр категории с использованием данных изображения
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRUDApiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRUDSerializer
    permission_classes = [IsAdminUser, ]
    lookup_field = "id"

'=============================================== Category ======================================================= '


class SubCategoryAllListApiView(ListAPIView):  # было 3 SQL запроса стало 2
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [SearchFilter]

   


class ListOneSubCategoryApiView(APIView):  # было 2 SQL запроса стало 1
    permission_classes = [AllowAny, ]
    serializer_class = SubCategoryListSerializer

    def get(self, request, id):  
        subcategory = SubCategory.objects.filter(id=id)
        serializer = CategoryListRUDSerializer(subcategory, many=True)
        return Response(serializer.data)



class SubCategoryCreateApiView(CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryCreateSerializer
    permission_classes = [IsAdminUser]


class SubCategoryRUDApiView(RetrieveUpdateDestroyAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer
    permission_classes = [IsAdminUser, ]
    lookup_field = "id"



class CategoryBySubCategory(APIView):  # было 2 SQL запроса стало 1
    permission_classes = [AllowAny, ]
    serializer_class = SubCategoryListSerializer

    def get(self, request, category_id):
        subcategory = SubCategory.objects.filter(category_id=category_id)
        serializer = SubCategoryListSerializer(subcategory, many=True)
        return Response(serializer.data)
    
    
    
