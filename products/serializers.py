from rest_framework import serializers
from .models import Product
from categories.serializers import CategoryListSerializer

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'amount', 'price', 'sale_price', 'bar_code')
        
        
class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'amount', 'price', 'sale_price', 'bar_code')