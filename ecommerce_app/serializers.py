from rest_framework.serializers import ModelSerializer
from .models import Category, SubCategory, Brand, Seller, Product, ProductType, Warranty


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class WarrantySerializer(ModelSerializer):
    class Meta:
        model = Warranty
        fields = '__all__'


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryBasedFilterSerializer(ModelSerializer):
    class Meta:
        model = Category
