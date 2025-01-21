from rest_framework import serializers
from .models import Product, Reviews, Inventory, Order
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
    ordered_items = serializers.JSONField()

    class Meta:
        model = Order
        fields = '__all__'