from rest_framework import serializers
from .models import Categeories ,Customer ,Customer_Detail ,Product ,ProductDetails

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categeories
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Detail
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
