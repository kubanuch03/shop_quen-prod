from rest_framework import serializers
from app_category.models import Category, SubCategory
from drf_spectacular.utils import extend_schema_field

class CategoryListRUDSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "title", "image"]



class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "image"]

    def validate(self, attrs):
        title = attrs['title']
        if Category.objects.filter(title=title).exists():
            raise serializers.ValidationError({"error":"Такое название уже существует"})
        return attrs





"======================================= CategorySerializers ========================="

class SubCategoryListSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = SubCategory
        fields = ["id", "title", "image"]



class SubCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ["id", "title", "image"]

    
    def validate(self, attrs):
        title = attrs['title']
        if SubCategory.objects.filter(title=title).exists():
            raise serializers.ValidationError({"error":"Такое название уже существует"})
        return attrs