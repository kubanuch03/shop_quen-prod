from rest_framework import serializers

from app_product.models import Product, Color, Size, CharacteristikTopik

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "sizes"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id','colors']

class CharacteristikSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacteristikTopik
        fields = ['id','title','value']
    
    def create(self, validated_data):
        title = validated_data['title']
        value = validated_data['value']

        if title.isdigit() or value.isdigit():
            raise serializers.ValidationError({"error":"title,value cannot contain is digit!"})
        return super().create(validated_data)
    
class ProductListSerializer(serializers.ModelSerializer):
    color =ColorSerializer(many=True)
    characteristics =CharacteristikSerializer(many=True)
    class Meta:
        model = Product
        fields = ["id",
                "subcategory",
                "title", 
                "price", 
                "description", 
                "brand", 
                "characteristics", 
                "is_any", 
                "images1", 
                "images2", 
                "images3", 
                "color",
                "size",
                "discount",
                "is_favorite",
                
]
    def to_representation(self, instance):
        data_product = super().to_representation(instance)        
        data_product['size'] = SizeSerializer(instance.size.all(), many=True).data
        data_product['color'] = ColorSerializer(instance.color.all(),many=True).data
        data_product['characteristics'] = CharacteristikSerializer(instance.characteristics.all(),many=True).data
        
        return data_product



class ProductcreateSerializer(serializers.ModelSerializer):
    discount = serializers.IntegerField(required=False)

    def apply_discount_to_price(self, price, discount):
        if discount > 0 and discount <= 100:
            discounted_price = price - (price * discount) // 100
            return discounted_price
        else:
            return price

    def create(self, validated_data):
        discount = validated_data.get('discount')
        price = validated_data['price']
        title = validated_data['title']
        brand = validated_data['brand']
        description = validated_data['description']

               
        
        if discount is not None:
            discounted_price = self.apply_discount_to_price(price, discount)
            validated_data['price'] = discounted_price
        
        if price is not None and price <= 0:
            raise serializers.ValidationError({"price": "Price must be a positive integer."})
        
        if (title.isdigit() or brand.isdigit() or description.isdigit()):
            raise serializers.ValidationError({"error":"title, brand, description cannot contain only digits."})



        return super().create(validated_data)

    
    
    class Meta:
        model = Product
        fields = ["id",
                "subcategory",
                "title", 
                "price", 
                "description", 
                "brand", 
                "characteristics", 
                "is_any", 
                "images1", 
                "images2", 
                "images3", 
                "color",
                "size",
                "discount",
]
        

