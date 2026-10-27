from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Product.
    """
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'stock', 'active', 'created_at', 'updated_at']
