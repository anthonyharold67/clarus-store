from rest_framework import serializers
from .models import Product,Category,ProductAll

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category= serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ("id","title","description","category", "category_id","price","quantity","image")


class ProductAllSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True,required=False)
    class Meta:
        model = ProductAll
        fields = ('id','name','product')
    
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        my_product = ProductAll.objects.create(**validated_data)
        for product in product_data:
            pas = Product.objects.create(**product)
            my_product.product.add(pas)
        my_product.save()
        return my_product